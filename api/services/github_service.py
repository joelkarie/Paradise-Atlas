import os
import base64

from github import Github, Auth, InputGitTreeElement
from github.GithubException import UnknownObjectException
from dotenv import load_dotenv

load_dotenv()


class GithubService:

    def __init__(self):
        auth = Auth.Token(os.getenv("GITHUB_TOKEN"))
        self.github = Github(auth=auth)

        owner = os.getenv("GITHUB_OWNER")
        repo = os.getenv("GITHUB_REPO")

        self.repo = self.github.get_repo(f"{owner}/{repo}")
        self.branch = os.getenv("GITHUB_BRANCH", "main")

    def upload_file(
        self,
        path: str,
        content: bytes,
        commit_message: str,
        content_type: str = "image/webp",
    ):
        try:
            existing = self.repo.get_contents(path, ref=self.branch)

            response = self.repo.update_file(
                path=path,
                message=commit_message,
                content=content,
                sha=existing.sha,
                branch=self.branch,
            )

            return {
                "action": "updated",
                "commit": response["commit"].sha,
            }

        except UnknownObjectException:
            response = self.repo.create_file(
                path=path,
                message=commit_message,
                content=content,
                branch=self.branch,
            )

            return {
                "action": "created",
                "commit": response["commit"].sha,
            }

    def upload_files_batch(
        self,
        files: list[dict],
        commit_message: str,
    ):
        """
        Upload multiple files in one Git commit.

        Each item in files must contain:
        - path: repository-relative file path
        - content: file bytes
        """

        if not files:
            raise ValueError("No files were provided.")

        # Get the current branch commit and its tree.
        branch_ref = self.repo.get_git_ref(f"heads/{self.branch}")
        parent_commit = self.repo.get_git_commit(
            branch_ref.object.sha
        )

        tree_elements = []

        for file in files:
            path = file["path"]
            content = file["content"]

            # GitHub Git Data API accepts Base64-encoded blob content.
            encoded_content = base64.b64encode(content).decode("ascii")

            blob = self.repo.create_git_blob(
                encoded_content,
                "base64",
            )

            tree_elements.append(
                InputGitTreeElement(
                    path=path,
                    mode="100644",
                    type="blob",
                    sha=blob.sha,
                )
            )

        # Preserve existing repository files and add/replace our images.
        new_tree = self.repo.create_git_tree(
            tree_elements,
            base_tree=parent_commit.tree,
        )

        # Create ONE commit containing every image.
        new_commit = self.repo.create_git_commit(
            commit_message,
            new_tree,
            [parent_commit],
        )

        # Move the branch to the new commit.
        branch_ref.edit(new_commit.sha)

        return {
            "action": "batch_uploaded",
            "count": len(files),
            "commit": new_commit.sha,
        }

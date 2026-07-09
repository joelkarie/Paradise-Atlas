import os
from github import Github, Auth
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

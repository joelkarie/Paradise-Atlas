
console.log("image_upload_batch.js loaded");

document.addEventListener("DOMContentLoaded", () => {
    const section = document.getElementById("batchImageUploadSection");
    const entity = section?.dataset.entity;

    const fileInput = document.getElementById("batchImageInput");
    const imageList = document.getElementById("batchImageList");
    const uploadButton = document.getElementById("batchUploadButton");
    const status = document.getElementById("batchUploadStatus");
    const locationOptions = document.getElementById("batchLocationOptions");

    if (!section || !fileInput || !imageList ||
        !uploadButton || !status || !locationOptions) {
        console.error("Batch upload HTML elements are missing.");
        return;
    }

    let selectedFiles = [];

    function createLocationDropdown() {
        const select = document.createElement("select");
        select.required = true;

        for (const option of locationOptions.options) {
            const copy = document.createElement("option");
            copy.value = option.value;
            copy.textContent = option.textContent.trim();
            select.appendChild(copy);
        }

        return select;
    }

    function renderFiles() {
        imageList.replaceChildren();

        selectedFiles.forEach((file, index) => {
            const row = document.createElement("div");
            row.style.display = "flex";
            row.style.alignItems = "center";
            row.style.gap = "12px";
            row.style.flexWrap = "wrap";
            row.style.marginBottom = "16px";

            const preview = document.createElement("img");
            preview.alt = `Preview of ${file.name}`;
            preview.style.width = "90px";
            preview.style.height = "70px";
            preview.style.objectFit = "cover";
            preview.src = URL.createObjectURL(file);

            const details = document.createElement("div");
            details.style.flex = "1";
            details.style.minWidth = "200px";

            const filename = document.createElement("div");
            filename.textContent = file.name;

            const recordLabel = document.createElement("label");
            recordLabel.textContent = "Assign location: ";
            recordLabel.style.display = "block";

            const locationSelect = createLocationDropdown();
            locationSelect.dataset.fileIndex = String(index);
            locationSelect.style.maxWidth = "100%";

            recordLabel.appendChild(locationSelect);
            details.append(filename, recordLabel);

            const removeButton = document.createElement("button");
            removeButton.type = "button";
            removeButton.textContent = "Remove";

            removeButton.addEventListener("click", () => {
                selectedFiles.splice(index, 1);
                renderFiles();
            });

            row.append(preview, details, removeButton);
            imageList.appendChild(row);
        });

        uploadButton.disabled = selectedFiles.length === 0;
        status.textContent = `${selectedFiles.length} image(s) selected.`;
    }

    fileInput.addEventListener("change", () => {
        selectedFiles.push(...Array.from(fileInput.files));
        fileInput.value = "";
        renderFiles();
    });

    uploadButton.addEventListener("click", async () => {
        const dropdowns = Array.from(
            imageList.querySelectorAll("select")
        );

        const recordIds = dropdowns.map(select => select.value);

        if (selectedFiles.length === 0) {
            status.textContent = "Select at least one image.";
            return;
        }

        if (recordIds.length !== selectedFiles.length ||
            recordIds.some(id => !id)) {
            status.textContent = "Assign a location to every image.";
            return;
        }

        if (new Set(recordIds).size !== recordIds.length) {
            status.textContent =
                "Each image must be assigned to a different location.";
            return;
        }

        const formData = new FormData();

        selectedFiles.forEach((file, index) => {
            formData.append("files", file);
            formData.append("ids", recordIds[index]);
        });

        uploadButton.disabled = true;
        fileInput.disabled = true;
        status.textContent = `Uploading ${selectedFiles.length} image(s)...`;

        try {
            const response = await fetch(
                `/images/admin/add_images_batch/${encodeURIComponent(entity)}`,
                {
                    method: "POST",
                    body: formData
                }
            );

            const result = await response.json().catch(() => ({}));

            if (!response.ok) {
                throw new Error(
                    result.detail || `Upload failed (${response.status})`
                );
            }

            status.textContent =
                `Uploaded ${result.count} image(s) in one GitHub commit. ` +
                `Commit: ${result.commit}`;

            selectedFiles = [];
            renderFiles();

        } catch (error) {
            console.error("Batch upload failed:", error);
            status.textContent = `Error: ${error.message}`;

        } finally {
            fileInput.disabled = false;
            uploadButton.disabled = selectedFiles.length === 0;
        }
    });

    console.log("Batch uploader initialized.");
});

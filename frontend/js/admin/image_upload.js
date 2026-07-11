console.log("image_upload.js loaded");

async function imageExists(url) {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
}
const TYPE_SINGULAR = {
    theatres: "theatre",
    locations: "location",
    visits: "visit",
    capitols: "capitol",
};

function typeId(typeName, typeId) {
    const singular = TYPE_SINGULAR[typeName] ?? typeName;
    return `static/images/${typeName}/${typeId}_${singular}.webp`;
}

document.addEventListener("DOMContentLoaded", () => {

    const uploadSection =
        document.getElementById("imageUploadSection");

    const entity =
        uploadSection.dataset.entity;

    console.log(entity);

    const idSelect =
        document.getElementById("imageIdSelect");

    const imagePreview =
        document.getElementById("idImagePreview");

    const uploadButton =
        document.getElementById("uploadIdImage");

    const imageInput =
        document.getElementById("idImageInput");

    console.log("In the function:");

    console.log(idSelect.value);

    // This page does not have the image section
    // so safely exit.
    if (!idSelect || !imagePreview) {
        console.log("In the return")
        return;
    }


    async function loadTheatreImage() {
        const imageId = idSelect.value;
        console.log("In loadTheatre1")
        if (!imageId) {
            console.log("In loadTheatre return")
            return;
        }

        const imageUrl = typeId(entity, imageId);
                console.log(imageUrl)

        try {
            if (await imageExists(imageUrl)) {
                imagePreview.src = imageUrl + "?v=" + Date.now();
            } else {
                imagePreview.src = "/static/assets/no_image.webp";
            }
            console.log("It worked")
        } catch (error) {
            console.error("Unable to load theatre image:", error);
            imagePreview.src = "/static/assets/no_image.webp";
        }
        console.log("Leaving load theatre function")
    }

    idSelect.addEventListener(
        "change",
        loadTheatreImage
    );


    // Load the first selected theatre immediately
    loadTheatreImage();



    if (uploadButton && imageInput) {

        uploadButton.addEventListener(
            "click",
            async () => {

                console.log(
                    "Upload button clicked"
                );


                const imageId =
                    idSelect.value;

                console.log(
                    imageId
                );
                const file =
                    imageInput.files[0];


                if (!file) {

                    alert(
                        "Please select an image first."
                    );

                    return;
                }
                else {
                    console.log("There is a file.")
                }


                const formData =
                    new FormData();


                formData.append(
                    "file",
                    file
                );


                try {
                    console.log("In try")
                    uploadButton.disabled = true;

                    uploadButton.innerText =
                        "Uploading...";

                    console.log("about to fetch")
                    const response =
                        await fetch(
                            `/images/admin/add_image/${entity}/${imageId}/image`,
                            {
                                method: "POST",
                                body: formData
                            }
                        );


                    if (!response.ok) {
                        console.log("Respone not ok")
                        let message =
                            "Upload failed";


                        try {

                            const error =
                                await response.json();

                            message =
                                error.detail ||
                                message;

                        }
                        catch {
                            console.log("In catch")
                            // Response was not JSON
                        }


                        throw new Error(message);
                    }

                    console.log("Awaiting response")
                    const result =
                        await response.json();


                    console.log(
                        "Upload result:",
                        result
                    );


                    imagePreview.src =
                        result.image_url +
                        "?v=" +
                        Date.now();


                    alert(
                        "Image uploaded successfully!"
                    );

                }
                catch (error) {

                    console.error(
                        "Upload error:",
                        error
                    );


                    alert(
                        error.message
                    );

                }
                finally {

                    uploadButton.disabled =
                        false;

                    uploadButton.innerText =
                        "Upload Image";
                }

            }
        );

    }

});
console.log("theatre_image_upload.js loaded");


document.addEventListener("DOMContentLoaded", () => {

    const theatreSelect =
        document.getElementById("imageTheatreSelect");

    const imagePreview =
        document.getElementById("theatreImagePreview");

    const uploadButton =
        document.getElementById("uploadTheatreImage");

    const imageInput =
        document.getElementById("theatreImageInput");


    // This page does not have the image section
    // so safely exit.
    if (!theatreSelect || !imagePreview) {
        return;
    }


    async function loadTheatreImage() {

        const theatreId = theatreSelect.value;

        if (!theatreId) {
            return;
        }


        try {

            const response = await fetch(
                `/theatres/${theatreId}/image`
            );


            if (!response.ok) {
                throw new Error(
                    "Unable to retrieve theatre image"
                );
            }


            const data = await response.json();


            imagePreview.src =
                data.url + "?v=" + Date.now();

        }
        catch (error) {

            console.error(
                "Unable to load theatre image:",
                error
            );

            imagePreview.src =
                "/static/assets/no_image.webp";
        }
    }


    theatreSelect.addEventListener(
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


                const theatreId =
                    theatreSelect.value;


                const file =
                    imageInput.files[0];


                if (!file) {

                    alert(
                        "Please select an image first."
                    );

                    return;
                }


                const formData =
                    new FormData();


                formData.append(
                    "file",
                    file
                );


                try {

                    uploadButton.disabled = true;

                    uploadButton.innerText =
                        "Uploading...";


                    const response =
                        await fetch(
                            `/admin/theatres/${theatreId}/image`,
                            {
                                method: "POST",
                                body: formData
                            }
                        );


                    if (!response.ok) {

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

                            // Response was not JSON
                        }


                        throw new Error(message);
                    }


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
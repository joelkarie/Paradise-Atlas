console.log("theatre_image_upload.js loaded");


document.addEventListener("DOMContentLoaded", () => {

    const uploadSection =
        document.getElementById("imageUploadSection");

    const entity =
        uploadSection.dataset.entity;

    console.log(entity);   // "theatre"

    const theatreSelect =
        document.getElementById("imageTheatreSelect");

    //     const imagePreview =
    //         document.getElementById("theatreImagePreview");

    const uploadButton =
        document.getElementById("uploadTheatreImage");

    const imageInput =
        document.getElementById("theatreImageInput");

    console.log("In the function:");
    console.log(theatreSelect.value);
    //     // This page does not have the image section
    //     // so safely exit.
    //     if (!theatreSelect || !imagePreview) {
    //         return;
    //     }


    //     async function loadTheatreImage() {

    //         const theatreId = theatreSelect.value;

    //         if (!theatreId) {
    //             return;
    //         }


    //         try {

    //             const response = await fetch(
    //                 `/theatres/${theatreId}/image`
    //             );


    //             if (!response.ok) {
    //                 throw new Error(
    //                     "Unable to retrieve theatre image"
    //                 );
    //             }


    //             const data = await response.json();


    //             imagePreview.src =
    //                 data.url + "?v=" + Date.now();

    //         }
    //         catch (error) {

    //             console.error(
    //                 "Unable to load theatre image:",
    //                 error
    //             );

    //             imagePreview.src =
    //                 "/static/assets/no_image.webp";
    //         }
    //     }


    //     theatreSelect.addEventListener(
    //         "change",
    //         loadTheatreImage
    //     );


    //     // Load the first selected theatre immediately
    //     loadTheatreImage();



    if (uploadButton && imageInput) {

        uploadButton.addEventListener(
            "click",
            async () => {

                console.log(
                    "Upload button clicked"
                );


                const theatreId =
                    theatreSelect.value;

                console.log(
                    theatreId
                );
                const file =
                    imageInput.files[0];


                if (!file) {

                    alert(
                        "Please select an image first."
                    );

                    return;
                }
                else
                {
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
                            `/theatres/admin/add_image/${theatreId}/image`,
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
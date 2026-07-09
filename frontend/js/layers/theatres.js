console.log("theatres.js loaded");

async function imageExists(url) {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
}

async function createTheatrePopupContent(theatre) {
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${theatre.name}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 2px;">
                ${theatre.city}, ${theatre.state_province}
            </div>
            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
            <div>
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            </div?>      
        </div>
            `;

    const imageUrl = `/static/images/theatres/${theatre.city.toLowerCase().replaceAll(" ", "_")}_theatre.webp`;

    if (await imageExists(imageUrl)) {
        html += `
            <a href="${imageUrl}" target="_blank">
                <img src="${imageUrl}" 
                    style="width:100%; max-width:400px; cursor:pointer;">
            </a>
                `;
    }

    return html;
}

export function createTheatreLayer(theatres) {
    const theatreLayer = L.layerGroup();

    theatres.forEach(theatre => {

        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/lk_logo.png"
                    style="
                        width:70px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [32, 43]
        });

        const marker = L.marker([
            theatre.latitude,
            theatre.longitude], { icon: customMarker })
            .addTo(theatreLayer);

        marker.on("click", async () => {
            const content = await createTheatrePopupContent(theatre);
            marker.bindPopup(content, { keepInView: true }).openPopup();
        });

    });
    return theatreLayer;

}

document.addEventListener("DOMContentLoaded", () => {

    const theatreSelect =
        document.getElementById("imageTheatreSelect");

    const imagePreview =
        document.getElementById("theatreImagePreview");

    const uploadButton =
        document.getElementById("uploadTheatreImage");

    const imageInput =
        document.getElementById("theatreImageInput");


    function loadTheatreImage() {

        const theatreId = theatreSelect.value;

        fetch(`/theatres/${theatreId}/image`)
            .then(response => response.json())
            .then(data => {

                imagePreview.src =
                    data.url + "?v=" + Date.now();

            })
            .catch(error => {
                console.error(
                    "Unable to load theatre image:",
                    error
                );
            });
    }


    if (theatreSelect && imagePreview) {

        theatreSelect.addEventListener(
            "change",
            loadTheatreImage
        );

        loadTheatreImage();
    }


    if (uploadButton && imageInput) {

        uploadButton.addEventListener(
            "click",
            async () => {
                console.log("Upload button clicked");
                const theatreId = theatreSelect.value;
                const file = imageInput.files[0];

                if (!file) {
                    alert("Please select an image first.");
                    return;
                }

                const formData = new FormData();

                formData.append(
                    "file",
                    file
                );


                try {

                    uploadButton.disabled = true;
                    uploadButton.innerText =
                        "Uploading...";


                    const response = await fetch(
                        `/admin/theatres/${theatreId}/image`,
                        {
                            method: "POST",
                            body: formData
                        }
                    );


                    if (!response.ok) {

                        const error =
                            await response.json();

                        throw new Error(
                            error.detail ||
                            "Upload failed"
                        );
                    }


                    const result =
                        await response.json();


                    imagePreview.src =
                        result.image_url +
                        "?v=" +
                        Date.now();


                    alert(
                        "Image uploaded successfully!"
                    );

                } catch (error) {

                    console.error(
                        "Upload error:",
                        error
                    );

                    alert(error.message);

                } finally {

                    uploadButton.disabled = false;
                    uploadButton.innerText =
                        "Upload Image";
                }

            }
        );

    }

});
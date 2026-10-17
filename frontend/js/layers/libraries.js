import { imageExists } from "./utils.js";

async function createLibraryPopupContent(library) {
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${library.name}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 2px;">
                ${library.state_province}, ${library.country}
            </div>
            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">     
        </div>
            `;

    const imageUrl = `/static/images/locations/${library.id}_location.webp`;

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

export function createLibrariesLayer(libraries) {
    const libraryLayer = L.layerGroup();

    libraries.forEach(library => {

        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/books.png"
                    style="
                        width:24px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconSize: [24, 24],
            iconAnchor: [12, 12]        });

        const marker = L.marker([
            library.latitude,
            library.longitude], { icon: customMarker })
            .addTo(libraryLayer);

        marker.on("click", async () => {
            const content = await createLibraryPopupContent(library);
            marker.bindPopup(content, {keepInView: true}).openPopup();
        });

    });
    return libraryLayer;

}

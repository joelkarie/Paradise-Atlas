import { imageExists } from "./utils.js";

async function createLocationLayerPopupContent(location) {
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${location.name}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 2px;">
                ${location.state_province}, ${location.country}
            </div>
            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">     
        </div>
            `;

    const imageUrl = `/static/images/locations/${location.id}_location.webp`;

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

export function createLocationLayer(locations, icon) {
    const locationLayer = L.layerGroup();

    locations.forEach(location => {

        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/${icon}"
                    style="
                        width:24px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconSize: [24, 24],
            iconAnchor: [12, 12]        });

        const marker = L.marker([
            location.latitude,
            location.longitude], { icon: customMarker })
            .addTo(locationLayer);

        marker.on("click", async () => {
            const content = await createLocationLayerPopupContent(location);
            marker.bindPopup(content, {keepInView: true}).openPopup();
        });

    });
    return locationLayer;

}

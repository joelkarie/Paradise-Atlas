async function createLocationsPopupContent(location) {
    console.log(location)
    let html = `
                <b>${location.name}</b><br>
                ${location.state_province}
            `;

    if (location.michael_highlights) {
        html += `
            <br>
            Michael's Highlights: ${location.michael_highlights}
                `;
    }

    if (location.joel_highlights) {
        html += `
            <br>
            Joel's Highlights: ${location.joel_highlights}
                `;
    }

    return html;
}

export function createLocationsLayer(locations) {
    const locationLayer = L.layerGroup();

    var stopNum = 1;
    locations.forEach(location => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/map_pin.png"
                    style="
                        width:30px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [15, 25]
        });
        const marker = L.marker([
            location.latitude,
            location.longitude], { icon: customMarker })
            .addTo(locationLayer);

        marker.on("click", async () => {
            const content = await createLocationsPopupContent(location);
            marker.bindPopup(content).openPopup();
        });
    });
    return locationLayer;
}

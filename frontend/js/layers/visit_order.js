async function createLocationsPopupContent(location, locations) {
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${location.name}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${location.state_province}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
        </div>`;

    if (location.visit_number > 1) {
        html += `
            <div>
                <span style="color: #5056cd; font-weight: 700;">Visiting From: </span>
                <span>${locations[location.visit_number - 1].name}, ${locations[location.visit_number - 1].state_province}</span>
            </div>
            `
    };

    if (location.visit_number < locations.length) {
        html += `
            <div>
                <span style="color: #5056cd; font-weight: 700;">Traveling To: </span>
                <span>${locations[location.visit_number + 1].name}, ${locations[location.visit_number + 1].state_province}</span>
            </div>
            `
    };

    return html;

}

export function createVisitOrderLayer(locations) {
    const visitOrderLayer = L.layerGroup();

    locations.sort((a, b) => a.visit_number - b.visit_number);

    locations.forEach(location => {
        const customMarker = L.divIcon({
            className: "numbered-marker",
            html: location.visit_number,
            iconSize: [35, 35],
            iconAnchor: [17, 35]

        });
        const marker = L.marker([
            location.latitude,
            location.longitude], { icon: customMarker })
            .addTo(visitOrderLayer);
        marker.on("click", async () => {
            const content = await createLocationsPopupContent(location, locations);
            marker.bindPopup(content).openPopup();
        });

    });

    const route = locations.map(location => [
        location.latitude,
        location.longitude
    ]);

    L.polyline(route, {
        color: "#a797a9",
        weight: 2
    }).addTo(visitOrderLayer);

    return visitOrderLayer;
}

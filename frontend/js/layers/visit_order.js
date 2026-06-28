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
        L.marker([
            location.latitude,
            location.longitude], { icon: customMarker })
            .addTo(visitOrderLayer)
            .bindPopup(`
                <b>${location.location_name}</b><br>
                ${location.state_province}
                ${location.date ? `<br><i>Visited on ${location.date}</i>` : ''}
            `);

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

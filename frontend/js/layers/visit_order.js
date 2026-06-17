export function createVisitOrderLayer(locations) {
    const visitOrderLayer = L.layerGroup();

    locations.forEach(location => {

        L.marker([
            location.latitude,
            location.longitude
        ])
            .addTo(visitOrderLayer)
            .bindPopup(`
                <b>${location.location_name}</b><br>
                ${location.state_province}
                ${location.date ? `<br><i>Visited on ${location.date}</i>` : ''}
            `);
    });
    return visitOrderLayer;
}
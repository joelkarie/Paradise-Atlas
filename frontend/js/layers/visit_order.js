export function createVisitOrderLayer(locations) {
    const visitOrderLayer = L.layerGroup();

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
    return visitOrderLayer;
}

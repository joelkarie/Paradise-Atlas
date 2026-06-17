export function createJoelCouldLiveLayer(cities) {
    const joelCouldLiveLayer = L.layerGroup();

    cities.forEach(city => {

        L.marker([
            city.latitude,
            city.longitude
        ])
            .addTo(joelCouldLiveLayer)
            .bindPopup(`
                <b>${city.name}</b><br>
                ${city.city}, ${city.state_province}
            `);

    });
    return joelCouldLiveLayer;
}
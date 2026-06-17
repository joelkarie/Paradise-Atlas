export function createCapitolLayer(capitols) {
    const capitolLayer = L.layerGroup();

    capitols.forEach(capitol => {

        L.marker([
            capitol.latitude,
            capitol.longitude
        ])
            .addTo(capitolLayer)
            .bindPopup(`
                <b>${capitol.name}</b><br>
                ${capitol.city}, ${capitol.state_province}
            `);

    });
    return capitolLayer;
}
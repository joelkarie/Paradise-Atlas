export function createJoelCouldLiveLayer(cities) {
    const joelCouldLiveLayer = L.layerGroup();

    cities.forEach(city => {
        const customMarker = L.divIcon({
            html: `
                <img src="assets/joel_in_dot_gray.png"
                    style="
                        width:45.8px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [38,43]
        });
        L.marker([
            city.latitude,
            city.longitude], { icon: customMarker })
            .addTo(joelCouldLiveLayer)
            .bindPopup(`
                <b>${city.city}</b><br>
                ${city.state_province}
            `);

    });
    return joelCouldLiveLayer;
}
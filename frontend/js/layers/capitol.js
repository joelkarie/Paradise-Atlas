export function createCapitolLayer(capitols) {
    const capitolLayer = L.layerGroup();

    capitols.forEach(capitol => {
        const customMarker = L.divIcon({
            html: `
                <img src="assets/capitol_marker.png"
                    style="
                        width:40px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [15,30]
        });

        L.marker([
            capitol.latitude,
            capitol.longitude
        ], {icon: customMarker})
            .addTo(capitolLayer)
            .bindPopup(`
                <b>${capitol.state_province} Capitol</b><br>
                ${capitol.city}, ${capitol.state_province}<br>
                Year Completed: ${capitol.year_completed}<br>
                Architect: ${capitol.architect}<br>
                Style: ${capitol.architectural_style}<br>
                Fact: ${capitol.fact}
                <img src="images/capitols/${capitol.state_province.toLowerCase().replace(/\s+/g, "_")}.webp" 
                width="300">
            `);

    });
    return capitolLayer;
}
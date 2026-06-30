export function createCapitolLayer(capitols, icon) {
    const capitolLayer = L.layerGroup();

    capitols.forEach(capitol => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/${icon}"
                    style="
                        width:40px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [15, 30]
        });

        L.marker([
            capitol.latitude,
            capitol.longitude
        ], { icon: customMarker })
            .addTo(capitolLayer)
            .bindPopup(`
                <div class="map-popup">
                <b>${capitol.state_province} Capitol</b><br>
                ${capitol.city}, ${capitol.state_province}<br>
                Year Completed: ${capitol.year_completed}<br>
                Architect: ${capitol.architect}<br>
                Style: ${capitol.architectural_style}<br>
                Fact: ${capitol.fact}
                <a href="/static/images/capitols/${capitol.state_province.toLowerCase().replace(/\s+/g, "_")}.webp"  target="_blank">
                     <img src="/static/images/capitols/${capitol.state_province.toLowerCase().replace(/\s+/g, "_")}.webp" 
                        style="width:100%; max-width:300px; cursor:pointer;">
                 </a>
                </d>
            `);

    });
    return capitolLayer;
}
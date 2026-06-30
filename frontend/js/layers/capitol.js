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

        let popup_info = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                <b>${capitol.state_province} Capitol</b><br>
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${capitol.city}, ${capitol.state_province}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">

            <div>
                Year Completed: ${capitol.year_completed}<br>
                Architect: ${capitol.architect}<br>
                Style: ${capitol.architectural_style}<br>
                Fact: ${capitol.fact}
                <a href="/static/images/capitols/${capitol.state_province.toLowerCase().replace(/\s+/g, "_")}.webp"  target="_blank">
                     <img src="/static/images/capitols/${capitol.state_province.toLowerCase().replace(/\s+/g, "_")}.webp" 
                        style="width:100%; max-width:300px; cursor:pointer;">
                 </a>
                </d>
            </div>

        </div>
        `

        L.marker([
            capitol.latitude,
            capitol.longitude
        ], { icon: customMarker })
            .addTo(capitolLayer)
            .bindPopup(popup_info, {keepInView: true});

    });
    return capitolLayer;
}
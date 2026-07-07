export function createDigsLayer(digs, icon) {
    const digsLayer = L.layerGroup();

    digs.forEach(digs => {
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
                <b>${digs.digs_type.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}</b><br>
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${digs.address}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">

        </div>
        `

        if (digs.name) {
            popup_info += `
            <div>
                ${digs.name}
            </div>
            `
        };
        L.marker([
            digs.latitude,
            digs.longitude
        ], { icon: customMarker })
            .addTo(digsLayer)
            .bindPopup(popup_info, { keepInView: true });

    });
    return digsLayer;
}
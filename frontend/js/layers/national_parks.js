export function createNationalParksLayer(parks, icon) {
    const nationalParksLayer = L.layerGroup();

    parks.forEach(park => {
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
                <b>${park.name}</b><br>
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${park.state_province}, ${park.country}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">


        </div>
        `

        L.marker([
            park.latitude,
            park.longitude
        ], { icon: customMarker })
            .addTo(nationalParksLayer)
            .bindPopup(popup_info, {keepInView: true});

    });
    return nationalParksLayer;
}

                // <a href="/static/images/capitols/${hotel.state_province.toLowerCase().replace(/\s+/g, "_")}.webp"  target="_blank">
                //      <img src="/static/images/capitols/${hotel.state_province.toLowerCase().replace(/\s+/g, "_")}.webp" 
                //         style="width:100%; max-width:300px; cursor:pointer;">
                //  </a>
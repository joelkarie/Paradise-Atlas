export function createCanadianRailwayHotelsLayer(hotels, icon) {
    const canadianRailwayHotelsLayer = L.layerGroup();

    hotels.forEach(hotel => {
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
                <b>${hotel.name}</b><br>
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${hotel.city}, ${hotel.province}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">

            <div>
                Year Opened: ${hotel.year_opened}<br>
                Architect: ${hotel.architect}<br>
                Railway Company: ${hotel.railway_company}<br>
                Fact: ${hotel.trivia}

                </d>
            </div>

        </div>
        `

        L.marker([
            hotel.latitude,
            hotel.longitude
        ], { icon: customMarker })
            .addTo(canadianRailwayHotelsLayer)
            .bindPopup(popup_info, {keepInView: true});

    });
    return canadianRailwayHotelsLayer;
}

                // <a href="/static/images/capitols/${hotel.state_province.toLowerCase().replace(/\s+/g, "_")}.webp"  target="_blank">
                //      <img src="/static/images/capitols/${hotel.state_province.toLowerCase().replace(/\s+/g, "_")}.webp" 
                //         style="width:100%; max-width:300px; cursor:pointer;">
                //  </a>
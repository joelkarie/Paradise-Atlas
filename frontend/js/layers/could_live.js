export function createCouldLiveLayer(cities, icon_filename, icon_size) {
    if (icon_size == undefined) { icon_size = 46 }
    const CouldLiveLayer = L.layerGroup();

    cities.forEach(city => {
        const customMarker = L.divIcon({
            html: `
            <img src="/static/assets/${icon_filename}"
                style="
                    width:${icon_size}px;
                    filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                ">
        `,
            className: "",
            iconAnchor: [38, 43]
        });
        L.marker([
            city.latitude,
            city.longitude], { icon: customMarker })
            .addTo(CouldLiveLayer)
            .bindPopup(`
                <div style="min-width: 260px; line-height: 1.4;">
                            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                                ${city.city}
                            </div>

                            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                                ${city.state_province}
                            </div>

                            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
                </div>
            `, {keepInView: true});

    });
    return CouldLiveLayer;
}

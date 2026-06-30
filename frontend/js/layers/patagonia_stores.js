export function createPatagoniaStoreLayer(stores) {
    const storeLayer = L.layerGroup();

    stores.forEach(store => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/patagonia_fish.png"
                    style="
                        width:65px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [38, 43]
        });
        L.marker([
            store.latitude,
            store.longitude], { icon: customMarker })
            .addTo(storeLayer)
            .bindPopup(`
                <div style="min-width: 260px; line-height: 1.4;">
                            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                                ${store.store_name}
                            </div>

                            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                                ${store.city}, ${store.state_province}
                            </div>

                            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
                </div>
            `, {keepInView: true});

    });
    return storeLayer;
}


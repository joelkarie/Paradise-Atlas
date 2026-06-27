export function createPatagoniaStoreLayer(stores) {
    const storeLayer = L.layerGroup();

    stores.forEach(store => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/patagonia_fish.png"
                    style="
                        width:76.8px;
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
                <b>${store.store_name}</b><br>
                ${store.city}, ${store.state_province}
            `);

    });
    return storeLayer;
}
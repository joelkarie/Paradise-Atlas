export function createPatagoniaStoreLayer(stores) {
    const storeLayer = L.layerGroup();

    stores.forEach(store => {

        L.marker([
            store.latitude,
            store.longitude
        ])
            .addTo(storeLayer)
            .bindPopup(`
                <b>${store.store_name}</b><br>
                ${store.city}, ${store.state_province}
            `);

    });
    return storeLayer;
}
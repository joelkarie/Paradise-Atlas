
export function createMap() {
    const isMobile = window.innerWidth < 768;

    const map = L.map('map', {
        maxBounds: [
            [-85, -180],
            [85, 180]
        ],
        maxBoundsViscosity: 1.0,
        zoomControl: !isMobile
    });
    map.setView(
        [39.5, -98.35],
        4
    );
    // Standard OpenStreetMap
    // L.tileLayer(
    //     'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    //     {
    //         attribution: '&copy; OpenStreetMap contributors'
    //     }
    // ).addTo(map);

    // Prettier Thunderforest tileset 
    L.tileLayer(
        'https://api.thunderforest.com/outdoors/{z}/{x}/{y}.png?apikey=REMOVED_API_KEY',
        {
            attribution: '&copy; Thunderforest &copy; OpenStreetMap contributors',
            maxZoom: 18
        }
    ).addTo(map);
    
    map.touchZoom.enable();
    map.doubleClickZoom.enable();
    map.scrollWheelZoom.disable();
    return map;
}
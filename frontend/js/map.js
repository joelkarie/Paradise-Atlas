
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
    // L.tileLayer(
    //     'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    //     {
    //         attribution: '&copy; OpenStreetMap contributors'
    //     }
    // ).addTo(map);
L.tileLayer(
    'https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg?api_key=REMOVED_API_KEY',
    {
        attribution:
            '&copy; Stadia Maps &copy; Stamen Design &copy; OpenStreetMap contributors',
        maxZoom: 16
    }
).addTo(map);
    map.touchZoom.enable();
    map.doubleClickZoom.enable();
    map.scrollWheelZoom.disable();
    return map;
}
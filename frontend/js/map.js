
export function createMap() {
    const map = L.map('map').setView(
        [39.5, -98.35],
        4
    );
    L.tileLayer(
        'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
            attribution: '&copy; OpenStreetMap contributors'
        }
    ).addTo(map);
    return map;
}

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


    L.tileLayer(
        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
        {
            attribution: 'Tiles &copy; Esri &mdash; Sources: Esri, Garmin, USGS, NGA, and others'
        }
    ).addTo(map);

    map.touchZoom.enable();
    map.doubleClickZoom.enable();
    map.scrollWheelZoom.disable();
    return map;
}
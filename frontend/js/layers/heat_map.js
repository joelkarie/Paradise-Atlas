
export function createHeatMapLayer(locations) {
    console.log("Testing createHeatMapLayer function.");
    let heatPoints = []

    locations.forEach(location => {
        let coordinates = [location.latitude, location.longitude]
        heatPoints.push(coordinates)
    });

    const heatLayer = L.heatLayer(heatPoints, {
    radius: 18,
    blur: 10,
    maxZoom: 12,
    max: 1.0
});

    const heatmapLayerGroup = L.layerGroup([heatLayer]);

    return heatmapLayerGroup;

}





export function createHeatMapLayer(locations) {

    const heatLayer = L.heatLayer(locations, {
    radius: 25,
    blur: 15,
    maxZoom: 12
});

    const heatmapLayerGroup = L.layerGroup([heatLayer]);

    return heatmapLayerGroup;

}

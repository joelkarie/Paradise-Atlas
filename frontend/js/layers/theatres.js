export function createTheatreLayer(theatres) {
    const theatreLayer = L.layerGroup();
    L.marker([39.5, -98.35]).addTo(theatreLayer).bindPopup("Theatres New");


    theatres.forEach(theatre => {

        L.marker([
            theatre.latitude,
            theatre.longitude
        ])
            .addTo(theatreLayer)
            .bindPopup(`
                <b>${theatre.name}</b><br>
                ${theatre.city}, ${theatre.state_province}
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            `);

    });
    return theatreLayer;

}
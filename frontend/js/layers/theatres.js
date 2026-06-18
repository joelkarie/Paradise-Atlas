export function createTheatreLayer(theatres) {
    const theatreLayer = L.layerGroup();

    theatres.forEach(theatre => {

        const customMarker = L.divIcon({
            html: `
                <img src="assets/lk_logo.png"
                    style="
                        width:70px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [38, 43]
        });
        L.marker([
            theatre.latitude,
            theatre.longitude], { icon: customMarker })
            .addTo(theatreLayer)
            .bindPopup(`
                <b>${theatre.name}</b><br>
                ${theatre.city}, ${theatre.state_province}
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            `);

    });
    return theatreLayer;

}
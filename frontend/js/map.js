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

const theatreLayer = L.layerGroup();

fetch("http://localhost:8000/theatres")
    .then(response => response.json())
    .then(theatres => {

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
        // theatreLayer.addTo(map);
    
    const overlays = {
        "Theatres": theatreLayer
    };
    L.control.layers(overlays).addTo(map);

    });
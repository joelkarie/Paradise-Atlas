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


fetch("http://localhost:8000/theatres")
    .then(response => response.json())
    .then(theatres => {

        theatres.forEach(theatre => {

            L.marker([
                theatre.latitude,
                theatre.longitude
            ])
            .addTo(map)
            .bindPopup(`
                <b>${theatre.name}</b><br>
                ${theatre.city}, ${theatre.state_province}
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            `);

        });

    });
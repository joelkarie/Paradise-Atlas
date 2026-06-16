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
    });
// theatreLayer.addTo(map);
const capitolLayer = L.layerGroup();

fetch("http://localhost:8000/capitols")
    .then(response => response.json())
    .then(capitols => {

        capitols.forEach(capitol => {

            L.marker([
                capitol.latitude,
                capitol.longitude
            ])
                .addTo(capitolLayer)
                .bindPopup(`
                <b>${capitol.city}, ${capitol.state_province}</b><br>
            `);

        });
    });


const joelCouldLiveLayer = L.layerGroup();

fetch("http://localhost:8000/joel-could-live")
    .then(response => response.json())
    .then(cities => {

        cities.forEach(city => {

            L.marker([
                city.latitude,
                city.longitude
            ])
                .addTo(joelCouldLiveLayer)
                .bindPopup(`
                <b>${city.city}, ${city.state_province}</b><br>
            `);

        }); 
    });


const vistitOrderLayer = L.layerGroup();

fetch("http://localhost:8000/visit-order")
    .then(response => response.json())
    .then(locations => {

        locations.forEach(location => {

            L.marker([
                location.latitude,
                location.longitude
            ])
                .addTo(vistitOrderLayer)
                .bindPopup(`
                <b>${location.name}</b><br>
                Visit Order: ${location.visit_number}
            `);

        }); 
    });

const overlays = {
    "Theatres": theatreLayer,
    "Capitols": capitolLayer,
    "Cities Joel Could Live In": joelCouldLiveLayer,
    "Visit Order": vistitOrderLayer
};
L.control.layers(overlays).addTo(map);

// });
async function imageExists(url) {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
}

async function createTheatrePopupContent(theatre) {
    let html = `
                <b>${theatre.name}</b><br>
                ${theatre.city}, ${theatre.state_province}
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            `;

    const imageUrl = `images/theatres/${theatre.city.toLowerCase().replaceAll(" ", "_")}_theatre.webp`;

    if (await imageExists(imageUrl)) {
        html += `
                    <img src="${imageUrl}" 
                        style="width:100%; max-width:400px;">
                `;
    }

    return html;
}

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

        const marker = L.marker([
            theatre.latitude,
            theatre.longitude], { icon: customMarker })
            .addTo(theatreLayer);

        marker.on("click", async () => {
            const content = await createTheatrePopupContent(theatre);
            marker.bindPopup(content).openPopup();
        });

    });
    return theatreLayer;

}
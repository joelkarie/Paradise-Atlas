async function imageExists(url) {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
}

async function createTheatrePopupContent(theatre) {
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${theatre.name}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${theatre.city}, ${theatre.state_province}
            </div>
            <div>
                ${theatre.date ? `<br><i>Visited on ${theatre.date}</i>` : ''}
            </div?>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
        </div>
            `;

    const imageUrl = `/static/images/theatres/${theatre.city.toLowerCase().replaceAll(" ", "_")}_theatre.webp`;

    if (await imageExists(imageUrl)) {
        html += `
            <a href="${imageUrl}" target="_blank">
                <img src="${imageUrl}" 
                    style="width:100%; max-width:400px; cursor:pointer;">
            </a>
                `;
    }

    return html;
}

export function createTheatreLayer(theatres) {
    const theatreLayer = L.layerGroup();

    theatres.forEach(theatre => {

        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/lk_logo.png"
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
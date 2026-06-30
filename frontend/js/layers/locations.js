async function createLocationsPopupContent(location) {
    const escapeHtml = (str) => {
        if (!str) return '';
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    };

    const state = escapeHtml(location.state_province || '');
    const joel_highlights = escapeHtml(location.joel_highlights || '');
    const michael_hightlights = escapeHtml(location.michael_highlights || '');

    // Basic Location Data
    let html = `
        <div style="min-width: 260px; line-height: 1.4;">
            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                ${escapeHtml(location.name)}
            </div>

            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                ${state}
            </div>

            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
        </div>`;

    // Rating Section
    if (location.joel_star_rating >= 1 || location.michael_star_rating >= 1) {
        html += `
        <div style="font-weight: 700; margin-bottom: 6px;">
            Rating:
        </div>
        `
    };

    if (location.joel_star_rating >= 1) {
        let stars = ``

        for (let i = 0; i < location.joel_star_rating; i++) {
            stars += `<div class="star-rating">★</div>`
        }
        html += `
        <div class="rating-row">
            <div class="person-label joel-label">Joel: </div>
            ${stars}
        </div>
        `
    };

    if (location.michael_star_rating >= 1) {
        let stars = ``

        for (let i = 0; i < location.michael_star_rating; i++) {
            stars += `<div class="star-rating">★</div>`
        }
        html += `
        <div class="rating-row" style="font-weight: 700; margin-bottom: 6px;">
            <div class="person-label michael-label">Michael: </div>
            ${stars}
        </div>
        `
    };

    // Highlights Section
    if (joel_highlights || michael_hightlights) {
        html += `
            <div style="font-weight: 700; margin-bottom: 6px;">
                Highlights:
            </div>
            `
    };
    if (michael_hightlights) {
        html += `
            <div>
                <span class="person-label michaek-label">Michael:</span>
                <span>${michael_hightlights || 'No highlights listed.'}</span>
            </div>
            `
    };
    if (joel_highlights) {
        html += `
            <div>
                <span class="person-label joel-label">Joel:</span>
                <span>${joel_highlights || 'No highlights listed.'}</span>
            </div>            
            `
    };

    return html;
}

export function createLocationsLayer(locations) {
    const locationLayer = L.layerGroup();

    var stopNum = 1;
    locations.forEach(location => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/map_pin_2.png"
                    style="
                        width:30px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [15, 25]
        });
        const marker = L.marker([
            location.latitude,
            location.longitude], { icon: customMarker })
            .addTo(locationLayer);

        marker.on("click", async () => {
            const content = await createLocationsPopupContent(location);
            marker.bindPopup(content, {keepInView: true}).openPopup();
        });
    });
    return locationLayer;
}

// async function createLocationsPopupContent(location) {
//     console.log(location)
//     let html = `
//                 <b>${location.name}</b><br>
//                 ${location.state_province}
//             `;

//     if (location.michael_highlights) {
//         html += `
//             <br>
//             Michael's Highlights: ${location.michael_highlights}
//                 `;
//     }

//     if (location.joel_highlights) {
//         html += `
//             <br>
//             Joel's Highlights: ${location.joel_highlights}
//                 `;
//     }

//     return html;
// }
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
    const joel_star_rating = escapeHtml(location.joel_star_rating || '');
    const michael_star_rating = escapeHtml(location.michael_star_rating || '');

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
        html +=`
        <div style="font-weight: 700; margin-bottom: 6px;">
            Highlights:
        </div>
        <div class="rating-row">
            <div class="subtitle">Joel: </div>
            <div class="${joel_star_rating >= 1 ? 'star star-rating' : 'star'}">★</div>
            <div class="${joel_star_rating >= 2 ? 'star star-rating' : 'star'}">★</div>
            <div class="${joel_star_rating >= 3 ? 'star star-rating' : 'star'}">★</div>
            <div class="${joel_star_rating >= 4 ? 'star star-rating' : 'star'}">★</div>
            <div class="${joel_star_rating >= 5 ? 'star star-rating' : 'star'}">★</div>
        </div>

        <div class="rating-row">
            <div class="${michael_star_rating >= 1 ? 'star star-rating' : 'star'}">★</div>
            <div class="${michael_star_rating >= 2 ? 'star star-rating' : 'star'}">★</div>
            <div class="${michael_star_rating >= 3 ? 'star star-rating' : 'star'}">★</div>
            <div class="${michael_star_rating >= 4 ? 'star star-rating' : 'star'}">★</div>
            <div class="${michael_star_rating >= 5 ? 'star star-rating' : 'star'}">★</div>
        </div>
        
        `;

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
                <span style="color: #1db1e7; font-weight: 700;">Michael:</span>
                <span>${michael_hightlights || 'No highlights listed.'}</span>
            </div>
            `
        };
        if (joel_highlights) {
            html +=`
            <div>
                <span style="color: #dc6e1a; font-weight: 700;">Joel:</span>
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
                <img src="/static/assets/map_pin.png"
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
            marker.bindPopup(content).openPopup();
        });
    });
    return locationLayer;
}

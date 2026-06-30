export function createQuakerMeetingsLayer(meetings) {
    const meetingLayer = L.layerGroup();

    meetings.forEach(meeting => {
        const customMarker = L.divIcon({
            html: `
                <img src="/static/assets/quaker_star.png"
                    style="
                        width:40px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [38, 43]
        });
        L.marker([
            meeting.latitude,
            meeting.longitude], { icon: customMarker })
            .addTo(meetingLayer)
            .bindPopup(`
                <div style="min-width: 260px; line-height: 1.4;">
                            <div style="font-size: 22px; font-weight: 700; margin-bottom: 2px;">
                                ${meeting.name}
                            </div>

                            <div style="font-size: 13px; color: #666; margin-bottom: 10px;">
                                ${meeting.city}, ${meeting.state_province}
                            </div>

                            <hr style="margin: 6px 0 10px 0; border: none; border-top: 1px solid #ddd;">
                </div>
            `, {keepInView: true});

    });
    return meetingLayer;
}


export function createQuakerMeetingsLayer(meetings) {
    const meetingLayer = L.layerGroup();

    meetings.forEach(meeting => {
        const customMarker = L.divIcon({
            html: `
                <img src="assets/quaker_star.png"
                    style="
                        width:50px;
                        filter: drop-shadow(2px 4px 3px rgba(0,0,0,0.4));
                    ">
            `,
            className: "",
            iconAnchor: [38,43]
        });
        L.marker([
            meeting.latitude,
            meeting.longitude], { icon: customMarker })
            .addTo(meetingLayer)
            .bindPopup(`
                <b>${meeting.naem}</b><br>
                ${meeting.city}, ${meeting.state_province}
            `);

    });
    return meetingLayer;
}
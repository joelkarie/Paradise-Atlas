export function createVisitOrderLayer(locations) {
    const visitOrderLayer = L.layerGroup();

    var stopNum = 1;
    locations.forEach(location => {
        const customMarker = L.divIcon({
            className: "numbered-marker",
            html: stopNum,
            iconSize: [35, 35],
            iconAnchor: [17, 35]  

        });
        L.marker([
            location.latitude,
            location.longitude], {icon: customMarker})
            .addTo(visitOrderLayer)
            .bindPopup(`
                <b>${location.location_name}</b><br>
                ${location.state_province}
                ${location.date ? `<br><i>Visited on ${location.date}</i>` : ''}
            `);
        stopNum += 1
    
    });
    const route = locations.map(location => [
        location.latitude,
        location.longitude
    ]);

    L.polyline(route, {
        color: "blue",
        weight: 4
    }).addTo(map);
    
    return visitOrderLayer;
}
    // # Number the cities in order of visit.
    // stop_num = 1

    // # Empty map
    // m = folium.Map(
    //     location=LOWER48_FOCUS_MAP_LOCATION[0],
    //     tiles="CartoDB Voyager",
    //     zoom_start=LOWER48_FOCUS_MAP_LOCATION[1],
    // )

    // script_monitor("Adding points to lines map for:", speak=False)
    // # Iterate through dataframe and add points to map
    // for city in range(0, len(df)):
    //     script_monitor(df.iloc[city]["City"], speak=False)
    //     icon_number = folium.plugins.BeautifyIcon(
    //         # border_color="#00ABCD",
    //         border_color="#b0c996",
    //         border_width=2,
    //         text_color="#000000",
    //         background_color="#fefdfd",
    //         number=stop_num,
    //         inner_icon_style="""
    //             display:flex;
    //             justify-content:center;
    //             align-items:center;
    //             font-size:12px;
    //             margin-top:1px;
    //         """,
    //     )
    //     folium.Marker(
    //         location=[df.iloc[city]["Latitude"], df.iloc[city]["Longitude"]],
    //         popup=df.iloc[city]["City"],
    //         icon=icon_number,
    //     ).add_to(m)
    //     stop_num += 1
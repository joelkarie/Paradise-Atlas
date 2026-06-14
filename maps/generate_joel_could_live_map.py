from api.app.services.joel_could_live_services import get_joel_could_live
import folium

BROAD_SCOPE_MAP_LOCATION_ZOOM = ([38.664067, -78.767974], 4)
LOWER48_FOCUS_MAP_LOCATION = ([38, -98], 4)


def make_joel_could_live_map(joel_could_live_locations):

    # Empty map centered on US
    m = folium.Map(
        location=LOWER48_FOCUS_MAP_LOCATION[0],
        tiles="OpenStreetMap",
        zoom_start=LOWER48_FOCUS_MAP_LOCATION[1],
    )

    # Iterate through joel_could_live_locations list and add points to map
    for city in joel_could_live_locations:

        lat = float(city["Latitude"])
        lon = float(city["Longitude"])
        name = city["City"]
        folium.Marker(location=[lat, lon], popup=name).add_to(m)

    m.save("maps/output/joel_could_live_map.html")


make_joel_could_live_map(get_joel_could_live())

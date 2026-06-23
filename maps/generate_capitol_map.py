from api.services.capitols_services import get_capitols
import folium
from maps.generate_visit_order_map import make_visit_order_map

BROAD_SCOPE_MAP_LOCATION_ZOOM = ([38.664067, -78.767974], 4)
LOWER48_FOCUS_MAP_LOCATION = ([38, -98], 4)


def make_capitol_map(capitol_locations):

    # Empty map centered on US
    m = folium.Map(
        location=LOWER48_FOCUS_MAP_LOCATION[0],
        tiles="OpenStreetMap",
        zoom_start=LOWER48_FOCUS_MAP_LOCATION[1],
    )

    # Iterate through capitol_locations list and add points to map
    for capitol in capitol_locations:

        lat = float(capitol["Latitude"])
        lon = float(capitol["Longitude"])
        name = capitol["City"]
        folium.Marker(location=[lat, lon], popup=name).add_to(m)

    m.save("maps/output/capitol_map.html")


make_capitol_map(get_capitols())

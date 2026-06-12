from api.app.services.visit_order_services import get_visit_order
import folium

BROAD_SCOPE_MAP_LOCATION_ZOOM = ([38.664067, -78.767974], 4)
LOWER48_FOCUS_MAP_LOCATION = ([38, -98], 4)


def make_visit_order_map(visit_order):

    # Empty map centered on US
    m = folium.Map(
        location=LOWER48_FOCUS_MAP_LOCATION[0],
        tiles="OpenStreetMap",
        zoom_start=LOWER48_FOCUS_MAP_LOCATION[1],
    )

    # Iterate through visit_order list and add points to map
    for visit in visit_order:

        lat = float(visit["Latitude"])
        lon = float(visit["Longitude"])
        name = visit["Location"]
        folium.Marker(location=[lat, lon], popup=name).add_to(m)

    m.save("maps/output/visit_order_map.html")


make_visit_order_map(get_visit_order())

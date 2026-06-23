from api.services.theatre_services import get_theatres
import folium
from folium.plugins import BeautifyIcon
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # TODO resolve basedir
BROAD_SCOPE_MAP_LOCATION_ZOOM = ([38.664067, -78.767974], 4)
LOWER48_FOCUS_MAP_LOCATION = ([38, -98], 4)


def make_theatres_map(theatres):

    # Empty map centered on US
    m = folium.Map(
        location=LOWER48_FOCUS_MAP_LOCATION[0],
        tiles=None,
        zoom_start=LOWER48_FOCUS_MAP_LOCATION[1],
    )

    # Iterate through theatres list and add points to map
    for theatre in theatres:

        icon = BeautifyIcon(
            icon="map-marker",
            icon_shape="marker",
            background_color="goldenrod",
            border_color="gray",
            text_color="ivory",
        )

        lat = theatre["latitude"]
        lon = theatre["longitude"]
        name = theatre["name"]
        folium.Marker(location=[lat, lon], icon=icon, popup=name).add_to(m)

    # Add Stadia tiles
    folium.TileLayer(
        tiles="https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png?api_key=REMOVED_API_KEY",
        attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>',
        name="Stadia Smooth",
        overlay=False,
        control=True,
    ).add_to(m)

    m.save("maps/output/theatres_map.html")


make_theatres_map(get_theatres())

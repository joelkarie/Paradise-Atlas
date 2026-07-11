TYPE_SINGULAR = {
    "theatres": "theatre",
    "locations": "location",
    "visits": "visit",
    "capitols": "capitol",
}


class ImagePaths:

    @staticmethod
    def theatre(theatre_id: int) -> str:
        return f"frontend/images/theatres/" f"{theatre_id}_theatre.webp"

    @staticmethod
    def type_id(type_name: str, type_id: int) -> str:
        singular = TYPE_SINGULAR.get(type_name, type_name)
        return f"frontend/images/{type_name}/{type_id}_{singular}.webp"

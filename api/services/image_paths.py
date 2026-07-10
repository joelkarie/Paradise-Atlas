class ImagePaths:

    @staticmethod
    def theatre(theatre_id: int) -> str:
        return f"frontend/images/theatres/" f"{theatre_id}_theatre.webp"
    @staticmethod
    def type_id(type_name:str, type_id: int) -> str:
        return f"frontend/images/{type_name}/" f"{type_id}_theatre.webp"

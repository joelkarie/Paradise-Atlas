from io import BytesIO
from PIL import Image, ImageOps


class ImageService:

    MAX_WIDTH = 1600
    QUALITY = 85

    @staticmethod
    def optimize(image_bytes: bytes) -> bytes:
        """
        Resize and optimize uploaded images.
        Returns WebP bytes.
        """

        image = Image.open(BytesIO(image_bytes))

        # Correct phone camera rotation
        image = ImageOps.exif_transpose(image)

        # Handle transparency
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA")

        # Resize while maintaining aspect ratio
        if image.width > ImageService.MAX_WIDTH:
            ratio = ImageService.MAX_WIDTH / image.width
            new_height = int(image.height * ratio)

            image = image.resize(
                (ImageService.MAX_WIDTH, new_height), Image.Resampling.LANCZOS
            )

        output = BytesIO()

        image.save(output, format="WEBP", quality=ImageService.QUALITY, method=6)

        return output.getvalue()

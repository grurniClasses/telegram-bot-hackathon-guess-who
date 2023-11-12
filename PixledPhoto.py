from PIL import Image

def pixelate_image(image_path, max_pixels):
    # טעינת התמונה
    with Image.open(image_path) as image:
        # חישוב גודל הפיקסל המתאים
        pixel_size = max(image.width, image.height) // max_pixels

        # חישוב המידות החדשות של התמונה על פי גודל הפיקסל
        small_image = image.resize(
            (image.width // pixel_size, image.height // pixel_size),
            resample=Image.BILINEAR,
        )

        # שינוי חזרה לגודל המקורי תוך כדי שמירה על הפיקסלציה
        result_image = small_image.resize(image.size, Image.NEAREST)

        return result_image

# If I don't need the original image, could modifying in place save some ressources?
from PIL import Image
import pygame


def remove_white_background(image_path, threshold=220):
    print(f"Path to image to be made transparent: {image_path}")
    img = Image.open(image_path)
    img = img.convert("RGBA")

    pixeldata = img.getdata()

    new_data = [
        (r, g, b, 0) if r > threshold and g > threshold and b > threshold else (r, g, b, a)
        for (r, g, b, a) in pixeldata
    ]

    img.putdata(new_data)
    return img

def pil_to_surface(pilImgage):
    return pygame.image.fromstring(
        pilImgage.tobytes(), pilImgage.size, pilImgage.mode
    ).convert_alpha()


def get_surface(pilImage):
    return pil_to_surface(pilImage)


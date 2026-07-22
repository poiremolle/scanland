# If I don't need the original image, could modifying in place save some ressources?
from threading import Thread
from queue import Queue
from screen import LandWindow
from PIL import Image
import pygame
from Creature import Creature 

class ImageProcessor:
    def __init__(self, input_queue, output_queue: Queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.working_thread = Thread(target=self.run)
    
    def start_image_processor(self):
        self.working_thread.start()

    def stop_image_processor(self):
        self.working_thread.stop()

    def queue_creature(self, path):
        self.input_queue.put(path)

    def run(self):
        while not self.input_queue.empty():
            path = self.input_queue.get()
            transparent_image = self.remove_white_background(path)
            surface_from_image = self.get_surface(transparent_image)
            self.land.queue_creature(surface_from_image)

    def remove_white_background(self, image_path, threshold=220):
        print(f"Path to image to be made transparent: {image_path}")

        img = Image.open(image_path)

        return self.make_white_pixels_transparent(img, threshold)

    def make_white_pixels_transparent(self, img, threshold):
        img = img.convert("RGBA")

        pixeldata = img.getdata()

        new_data = [
            (r, g, b, 0) if r > threshold and g > threshold and b > threshold else (r, g, b, a)
            for (r, g, b, a) in pixeldata
        ]

        img.putdata(new_data)

        return img


    def pil_to_surface(self, pilImgage):
        return pygame.image.fromstring(
            pilImgage.tobytes(), pilImgage.size, pilImgage.mode
        ).convert_alpha()


    def get_surface(self, pilImage):
        return self.pil_to_surface(pilImage)


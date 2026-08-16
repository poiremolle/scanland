# If I don't need the original image, could modifying in place save some ressources?
from threading import Thread
from queue import Queue
from PIL import Image
import pygame

class ImageProcessor:
    def __init__(self, input_queue: Queue, output_queue: Queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.processing_thread = Thread(target=self.run)
        self.processing_thread.start()

    def run(self):
        while True:
            path = self.input_queue.get()

            if path is None:
                break

            self.output_queue.put(self.process_image(path))

    def stop(self):
        self.input_queue.put(None)
        self.processing_thread.join()
      
    def process_image(self, path):
        transparent_image = self.remove_white_background(path)
        return self.pil_to_tuple(transparent_image)
        #return self.get_surface(transparent_image)
    
    # def queue_image(self, surface):
    #     self.output_queue.put(surface)

    def remove_white_background(self, image_path, threshold=220):
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
    
    def pil_to_tuple(self, pilImage):
        return (pilImage.toBytes(), pilImage.size, pilImage.mode)

    def get_surface(self, pilImage):
        return self.pil_to_surface(pilImage)
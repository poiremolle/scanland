# If I don't need the original image, could modifying in place save some ressources?
from threading import Thread
from queue import Queue
from PIL import Image
from scanland.constants import MAX_IMAGE_HEIGHT

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
        img = Image.open(path)
        
        resized_image = self.resize_image(img)
        transparent_image = self.make_white_pixels_transparent(resized_image)

        return self.pil_to_tuple(transparent_image)
    
    def resize_image(self, img):
        max_size = (MAX_IMAGE_HEIGHT, MAX_IMAGE_HEIGHT)
        img.thumbnail(max_size)
        return img

    def remove_white_background(self, img, threshold=220):
        return self.make_white_pixels_transparent(img, threshold)

    def make_white_pixels_transparent(self, img, threshold=220):   
        img = img.convert("RGBA")

        pixeldata = img.getdata()

        new_data = [
            (r, g, b, 0) if r > threshold and g > threshold and b > threshold else (r, g, b, a)
            for (r, g, b, a) in pixeldata
        ]

        img.putdata(new_data)

        return img
    
    def pil_to_tuple(self, pilImage):
        return (pilImage.tobytes(), pilImage.size, pilImage.mode)
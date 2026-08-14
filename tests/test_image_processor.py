import pytest
from queue import Queue
from scanland.image_processor import ImageProcessor
from PIL import Image

# @pytest.fixture
# def processor():
#     test_input_queue = Queue()
#     test_output_queue = Queue()

#     return ImageProcessor(test_input_queue, test_output_queue)

# def test_queue_image(processor):
#     surface = ImageProcessor.get_surface(
#         Image.open("test/test_assets/appleworm.jpg")
#     )
    
#     ImageProcessor.queue_image(surface)

#     assert processor.test_output_queue.qsize() == 1

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
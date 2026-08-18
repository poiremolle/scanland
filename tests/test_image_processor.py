import pytest
from queue import Queue
from scanland.image_processor import ImageProcessor
from PIL import Image

@pytest.fixture
def image_processor():
    input_queue = Queue()
    output_queue = Queue()
    return ImageProcessor(input_queue, output_queue)

def test_resize_image(image_processor):
    img = Image.open("tests/test_assets/appleworm.jpg")

    image_processor.resize_image(img)

    assert img.height == 400
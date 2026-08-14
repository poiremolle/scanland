import pytest
from queue import Queue
from scanland.image_processor import ImageProcessor

@pytest.fixture
def processor():
    test_input_queue = Queue()
    test_output_queue = Queue()

    return ImageProcessor(test_input_queue, test_output_queue)
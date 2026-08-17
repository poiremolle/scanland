import pytest
from queue import Queue
from scanland.file_watcher import MyEventHandler
from PIL import Image

@pytest.fixture
def file_watcher():
    input_queue = Queue()
    return MyEventHandler(input_queue)

def test_is_image_suffix_true(file_watcher):
    assert file_watcher.is_image_suffix("test.png") == True
    assert file_watcher.is_image_suffix("test.PNG") == True
    assert file_watcher.is_image_suffix("test.jpg") == True
    assert file_watcher.is_image_suffix("test.JPG") == True
    assert file_watcher.is_image_suffix("test.jpeg") == True
    assert file_watcher.is_image_suffix("test.JPEG") == True


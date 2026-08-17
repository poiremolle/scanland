import pytest
from queue import Queue
from scanland.file_watcher import MyEventHandler
from PIL import Image

@pytest.fixture
def file_watcher():
    input_queue = Queue()
    return MyEventHandler(input_queue)

def test_is_image_suffix(file_watcher):
    assert file_watcher.is_image_suffix("test.png") == True

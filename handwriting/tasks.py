from __future__ import absolute_import
from celery import shared_task
import pyocr
import pyocr.builders
from PIL import Image

TOOL = pyocr.get_available_tools()[0]
LANGUAGE = TOOL.get_available_languages()[12]


@shared_task
def get_text_from_image(image):
    text = TOOL.image_to_string(Image.open(image),
                                lang=LANGUAGE,
                                builder=pyocr.builders.TextBuilder())



    return text

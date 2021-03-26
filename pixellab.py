import os
from PIL import Image
from PIL.ExifTags import TAGS

from exif_keys import exif_keys

from django.conf import settings

BASE_DIR = settings.MEDIA_ROOT


def pixel_analyse(image_path):
    # path to the image or video
    imagename = image_path.lstrip('/')

    # read the image data using PIL
    image = Image.open(imagename)

    # extract EXIF data
    exifdata = image.getexif()

    # Initialize the result dict
    result_dict = dict()

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)

        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()

        # Check if the tag is in exif_keys
        if tag in exif_keys.keys():
            print(exif_keys[tag], data)
            data = exif_keys[tag].get(str(data))
        
        # Adding the data to the result dict
        result_dict[tag] = str(data)

    return result_dict
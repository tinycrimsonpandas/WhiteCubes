'''
resize the user uploaded images to make progressive and faster loading jpgs
'''
from os import path
from glob import glob
from PIL import Image


def image_resize():
    '''
    generate optimized images for thumbnails
    '''
    images = [x for x in glob("static/images/**") if not path.isdir(x)]
    thumbnails = [
        path.basename(x) for x in glob("static/images/thumbnails/**")
    ]

    for image in images:
        # check if the image already has a thumbnail
        if path.basename(image) in thumbnails:
            continue
        
        # if it doesn't then generate one and put it in the thumbnail folder
        with Image.open(image) as image_open:
            if image_open.width > 900:
                size = 1000, 1000
                image_open.thumbnail(size)
            image_open.save(
                f"{path.dirname(image)}/thumbnails/{path.basename(image)}",
                "JPEG",
                quality=95,
                optimize=True,
                progressive=True)

from glob import glob
from PIL import Image
from os import path


def image_resize():
    # generate optimized images for thumbnails
    images = [x for x in glob("static/images/**") if path.isdir(x) == False]
    thumbnails = [
        path.basename(x) for x in glob("static/images/thumbnails/**")
    ]

    for image in images:
        if path.basename(image) in thumbnails:
            continue
        else:
            with Image.open(image) as im:
                if im.width > 900:
                    size = 1000, 1000
                    im.thumbnail(size)
                im.save(
                    f"{path.dirname(image)}/thumbnails/{path.basename(image)}",
                    "JPEG",
                    quality=95,
                    optimize=True,
                    progressive=True)

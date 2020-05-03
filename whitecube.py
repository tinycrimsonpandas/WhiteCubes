from sys import argv
from flask_frozen import Freezer
from glob import glob
from os import path, rename

from resize import image_resize
from server import app

freezer = Freezer(app)

# make sure to generate thumbnails if they haven't already
image_resize()


#generate all of the URLS that we need to make sure to make pages for
@freezer.register_generator
def site_pages():
    page = [
        f"{path.splitext(path.basename(x))[0]}"
        for x in glob("pages/**", recursive=True) if path.isdir(x) == False
    ]
    for page in page:
        if page != "index" and page != '404':
            yield {'path': page}
    yield {'path': '/'}

#generate the 404 error
@freezer.register_generator
def error_handlers():
    yield "/404"

if __name__ == '__main__':
    if len(argv) == 1:
        freezer.freeze()
        rename('build/404', 'build/404.html')
    else:
        if argv[1] == 'preview':
            freezer.run()
            rename('build/404', 'build/404.html')
        else:
            print(
                "Accepts either no input to build the static site or use the argument [preview] to build then launch a local webserver"
            )

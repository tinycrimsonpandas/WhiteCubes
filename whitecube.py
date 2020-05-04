'''
generate a list of urls to be frozen
then freeze and optionally serve the statically generated site
'''

from sys import argv
from glob import glob
from os import path, rename
from flask_frozen import Freezer

from resize import image_resize
from server import app

freezer = Freezer(app)

# make sure to generate thumbnails if they haven't already
image_resize()


# generate all of the URLS that we need to make sure to make pages for
@freezer.register_generator
def site_pages():
    '''
    crawl the appropriate file directories to get all the pages to freeze
    '''
    page = [
        f"{path.splitext(path.basename(x))[0]}"
        for x in glob("pages/**", recursive=True) if not path.isdir(x)
    ]
    for page in page:
        if page not in ('index', '404'):
            yield {'path': page}
    yield {'path': '/'}


# generate the 404 error
@freezer.register_generator
def error_handlers():
    '''
    freeze the 404 page
    '''
    yield "/404"


if __name__ == '__main__':
    # enable the preview option or print help
    if len(argv) == 1:
        freezer.freeze()
        rename('build/404', 'build/404.html')
    else:
        if argv[1] == 'preview':
            freezer.run()
            rename('build/404', 'build/404.html')
        else:
            print(
                "Only accepts [preview] as an argument, which serves the built site"
            )

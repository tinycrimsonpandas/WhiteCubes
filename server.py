'''
use flask and flask-flatpages to render the static content
'''
import os
from flask import Flask, render_template
from flask_flatpages import FlatPages
import yaml

# Configure application
app = Flask(__name__)

# Configure flatpages and image resize
pages = FlatPages(app)

# import the config files
with open("settings/nav.yml", 'r') as nav_file:
    nav = yaml.load(nav_file, Loader=yaml.SafeLoader)

with open('settings/site.yml', 'r') as site_file:
    site = yaml.load(site_file, Loader=yaml.SafeLoader)


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>/", methods=["GET"])
def site_pages(path):
    '''
    take the input path and render the appropriate gallery or page
    '''
    if path == '':
        path = 'index'

    # first check if there is a page, then check if there is a gallery
    page = pages.get(f"text/{path}")
    if page is None:
        page = pages.get_or_404(f"galleries/{path}")
        # append the thumbnails to the page
        for image in page['images']:
            thumb = f"{os.path.dirname(image['url'])}/thumbnails/{os.path.basename(image['url'])}"
            image['thumbnail'] = thumb

    return render_template(page.meta['template'],
                           page=page,
                           site=site,
                           nav=nav)


@app.errorhandler(404)
def not_found():
    '''
    render the 404 error page!
    '''
    page = pages.get("text/404.html")

    return render_template(page.meta['template'],
                           page=page,
                           site=site,
                           nav=nav)

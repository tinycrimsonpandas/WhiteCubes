from flask import Flask, flash, jsonify, redirect, render_template, request, send_from_directory, abort
from flask_flatpages import FlatPages
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError, NotFound
import yaml

# Configure application
app = Flask(__name__)

# Configure flatpages and image resize
pages = FlatPages(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# import the config files
with open("settings/nav.yml", 'r') as nav_file:
    nav = yaml.load(nav_file, Loader=yaml.SafeLoader)

with open('settings/site.yml', 'r') as site_file:
    site = yaml.load(site_file, Loader=yaml.SafeLoader)


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>/", methods=["GET"])
def site_pages(path):

    if path == '':
        path = 'index'

    # first check if there is a page, then check if there is a gallery
    page = pages.get(f"text/{path}")
    if page == None:
        page = pages.get_or_404(f"galleries/{path}")
        # append the thumbnails to the page
        for image in page['images']:
            thumb_path = f"{os.path.dirname(image['url'])}/thumbnails/{os.path.basename(image['url'])}"
            image['thumbnail'] = thumb_path

    return render_template(page.meta['template'],
                           page=page,
                           site=site,
                           nav=nav)


@app.errorhandler(404)
def not_found(e):
    page = pages.get("text/404.html")

    return render_template(page.meta['template'],
                           page=page,
                           site=site,
                           nav=nav)

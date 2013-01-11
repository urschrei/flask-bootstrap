import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import YAMLLoader
import locale
import logging


app = Flask(__name__)
# attach DB. This assumes a Blueprint model
from apps.shared.models import db
db.init_app(app)

# load configs
app.config.from_pyfile('config/default.cfg')
# dev config will override anything set on line above
if os.getenv('DEV_CONFIGURATION'):
    app.config.from_envvar('DEV_CONFIGURATION')

# attach assets
assets = Environment(app)
assets.versions = 'hash'
assets.url = app.static_url_path
manifest_path = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '.static-manifest'))
assets.manifest = 'file://%s' % manifest_path
bundles = YAMLLoader(os.path.realpath(
    os.path.join(os.path.dirname(__file__), 'assets.yml'))).load_bundles()
for bundle_name, bundle in bundles.items():
    assets.register(bundle_name, bundle)

# set up logging
if not app.debug:
    log_format = logging.Formatter("""
---
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Time:               %(asctime)s

%(message)s

""")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)
    app.logger.addHandler(stream_handler)


## import blueprint(s), and attach. Do this for each blueprint
from apps.example.views import example
app.register_blueprint(example, url_prefix='/example')

# Example route
@app.route("/", methods=["GET"])
def index():
    """ Example index """
    return render_template('index.jinja')

# set up error handling pages
@app.errorhandler(404)
def page_not_found(error):
    """ 404 handler """
    return render_template(
        'errors/404.jinja'), 404

@app.errorhandler(500)
def application_error(error):
    """ 500 handler """
    return render_template(
        'errors/500.jinja'), 500

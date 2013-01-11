import os
from flask import current_app
from flask import (
    Blueprint,
    request,
    flash,
    render_template,
    send_file,
    jsonify,
    )

from models import *
from forms import *

example = Blueprint(
    'example',
    __name__,
    template_folder='templates'
    )

@example.route('/', methods=['GET'])
def toplevel():
    """ Example Blueprint index """
    return render_template('example.jinja')

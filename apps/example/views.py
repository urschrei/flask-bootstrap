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

from flask.ext.bcrypt import Bcrypt

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
    # bcrypt can be used inside the view function
    bcrypt = Bcrypt(current_app)
    # now you can do e.g. bcrypt.generate_password_hash('foo')
    return render_template('example.jinja')

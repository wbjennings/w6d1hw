from flask import render_template
from . import bp 

@bp.route('/inventory')
def inventory():
    return render_template('inventory.jinja')
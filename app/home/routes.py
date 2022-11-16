from flask import Blueprint, render_template
from flask import current_app as app

home_blueprint = Blueprint(
    name='home_bp',
    import_name=__name__,
    static_folder='static',
    template_folder='templates'
)

@home_blueprint.route('/', methods=['GET'])
def home():
    """Home/Landing page"""
    return render_template(
        'index.jinja2',
        title='Bookly | Home'
    )
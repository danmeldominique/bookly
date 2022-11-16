from flask import Flask
from flask_assets import Environment
def init_app():
    """Initialise core application"""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfiguration')
    
    # Initialise plugins
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Route imports
        from .home.routes import home_blueprint
        from .assets import compile_assets

        # Register Blueprints
        app.register_blueprint(home_blueprint)

        # Compile static files
        compile_assets(assets)
        return app
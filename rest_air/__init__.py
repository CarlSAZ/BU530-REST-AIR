'''This is a basic template for an API App that works with pytest'''
from apiflask import APIFlask, HTTPBasicAuth
from flask_redis import FlaskRedis

auth = HTTPBasicAuth()

rdb = FlaskRedis()

def create_app(configObject='config.DevConfig'):
    app = APIFlask(__name__,instance_relative_config=False)
    app.config.from_object(configObject)
    rdb.init_app(app)
    
    with app.app_context():
        # Include routes if any
        from . import routes

        # Register blueprints
        app.register_blueprint(routes.landing)
        return app

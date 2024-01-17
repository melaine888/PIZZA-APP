from flask import Flask 
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from flask_restx import Api
from .utils import db
from .models.orders import Order
from .models.users import User
from flask_migrate import Migrate


def create_app(config=config_dict['dev']):
    
    #Create an instance of the Flask application
    app=Flask(__name__)
    
    #Load configuration from the provided dictionary
    app.config.from_object(config)
    
    #Initialize the Flask application with the SQLAlchemy database.
    db.init_app(app)
    
    # Create an instance of Migrate and associate it with the Flask application (app) and the SQLAlchemy instance (db).
    migrate = Migrate(app,db)
    
    api=Api(app)
    
    
    #Register Namespaces
    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path = '/auth')
    
    
    @app.shell_context_processor
    def make_shell_context():
        return{
            'db':db,
            'User':User,
            'Orders':Order
        }
    
    return app
from flask import Flask 
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from flask_restx import Api


def create_app(config=config_dict['dev']):
    
    #Create an instance of the Flask application
    app=Flask(__name__)
    
    #Load configuration from the provided dictionary
    app.config.from_object(config)
    
    api=Api(app)
    
    
    #Register Namespaces
    
    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path = '/auth')
    
    return app
from flask import Flask 
from .orders.views import order_namespace
from .auth.views import auth_namespace
from flask_restx import Api

def create_app():
    app=Flask(__name__)
    
    api=Api(app)
    
    api.add_namespace(order_namespace,path = '/')
    api.add_namespace(auth_namespace, path = '/auth')
    
    return app
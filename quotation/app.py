'''入口'''

from flask import Flask, jsonify
from .futures import api as futures_api
from .extensions import init_db
from . import config


def create_app():
    """Create a Flask app."""
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        '''d'''
        return 'Hello World! 233!'

    if config is not None:    
        app.config.from_object(config)
    
    #起数据库
    init_db(app)

    #起blueprint或者restful api
    #app.register_blueprint(futures_bp)
    futures_api.init_app(app)

    return app
from flask import Flask, jsonify
from extensions import db

def create_app(config=None):
    """Create a Flask app."""
    app = Flask(__name__)

    #app.register_blueprint(simple_page)

    return app
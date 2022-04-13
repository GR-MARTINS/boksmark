from flask import Flask
from bookmarks import config
from bookmarks.auth import auth
from bookmarks.bookmarks import bookmarks

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    return app

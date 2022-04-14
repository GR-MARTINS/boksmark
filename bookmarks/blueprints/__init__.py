from bookmarks.blueprints.auth import auth
from bookmarks.blueprints.bookmarks import bookmarks


def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

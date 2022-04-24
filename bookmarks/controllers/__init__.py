from bookmarks.controllers.api.auth import auth
from bookmarks.controllers.api.bookmarks import bookmarks


def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

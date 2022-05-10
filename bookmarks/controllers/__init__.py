from bookmarks.controllers.auth import auth
from bookmarks.controllers.bookmarks import bookmarks


def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)


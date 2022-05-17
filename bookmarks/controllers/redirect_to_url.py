from bookmarks.models.tables.bookmarks import Bookmark
from bookmarks.models.tables.visits import Visit
from bookmarks.ext.sqlalchemy import db
from flasgger import swag_from
from flask import redirect


def init_app(app):

    @app.get('/<short_url>')
    @swag_from('../docs/short_url.yaml')
    def redirect_to_url(short_url):
        bookmark = Bookmark.query.filter_by(short_url=short_url).first_or_404()

        if bookmark:
            bookmark.visits = bookmark.visits + 1
            visit = Visit(bookmark_id=bookmark.id)
            db.session.add(visit)
            db.session.commit()

            return redirect(bookmark.url)

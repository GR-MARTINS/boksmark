from datetime import datetime
from bookmarks.ext.sqlalchemy import db


class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    bookmark_id = db.Column(db.Integer, db.ForeignKey('bookmarks.id'))
    visiting_hours = db.Column(db.DateTime, default=datetime.now())

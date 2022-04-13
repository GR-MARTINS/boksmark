from flask import Blueprint


bookmarks = Blueprint("bookmaks", __name__, url_prefix="/api/v1/bookmarks")


@bookmarks.get('/')
def get_all():
    return {"bookmarks": []}

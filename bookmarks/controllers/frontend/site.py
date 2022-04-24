from flask import (
    Blueprint,
    render_template
)
from bookmarks.models.forms.login_form import Login

site = Blueprint("site", __name__)


@site.route('/')
def index():
    return render_template("index.html")


@site.route('/login')
def login():
    form = Login()
    return render_template("login.html", form=form)


@site.route('/register')
def register():
    return "register"
import wtforms as wtf
from flask_wtf import FlaskForm


class Login(FlaskForm):
    email = wtf.EmailField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField(
        "Password", [wtf.validators.DataRequired()]
    )
    remember = wtf.BooleanField("Remember-me")

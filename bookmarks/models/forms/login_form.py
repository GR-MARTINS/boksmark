import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class Login(FlaskForm):
    email = wtf.EmailField(
        "E-mail", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    passwd = wtf.PasswordField(
        "Senha", [wtf.validators.DataRequired()]
    )
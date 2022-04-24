import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class Login(FlaskForm):
    username= wtf.StringField(
        "Senha", [wtf.validators.DataRequired()]
    )    
    email = wtf.EmailField(
        "E-mail", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField(
        "Senha", [wtf.validators.DataRequired()]
    )
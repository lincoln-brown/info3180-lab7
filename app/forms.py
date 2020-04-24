
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import InputRequired
from wtforms import StringField

class UploadForm(FlaskForm):
    photo=FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png'])])
    description =StringField('Description', validators=[InputRequired()])
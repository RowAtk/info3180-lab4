from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):

    image = FileField(
        label=u"File upload", 
        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], message="Image Files Only")]
        )
    
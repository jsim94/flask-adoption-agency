from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, URLField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange
from wtforms.widgets import TextArea


class AddPet(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField('Species')
    photo_url = URLField('Photo URL')
    age = IntegerField('Age', validators=[NumberRange(min=None, max=None, )])
    notes = StringField('Notes')
    available = BooleanField('Available', default=True)


class EditPet(FlaskForm):

    photo_url = URLField('Photo URL')
    notes = StringField('Notes', widget=TextArea())
    available = BooleanField('Available', default=True)

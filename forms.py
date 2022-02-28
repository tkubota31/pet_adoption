from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for creating new pets"""
    name = StringField("Pet_name", validators=[InputRequired()])
    species = SelectField("Species", choices =[("cat", "cat"), ("dog","dog"),("porcupine","porcupine")])
    photo_url = StringField("Photo URL", validators =[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators =[Optional()])

class EditPetForm(FlaskForm):
    """form to edit existing pet"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateEntryForm(FlaskForm):
    entry = TextAreaField('Entry', validators=[DataRequired(), Length(min=5)], render_kw={'placeholder': 'Entry'})
    submit = SubmitField('Save')

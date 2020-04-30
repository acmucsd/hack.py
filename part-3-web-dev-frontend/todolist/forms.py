from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Item')
class DeleteForm(FlaskForm):
    submit = SubmitField('Pop Item')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EnterIdPredict(FlaskForm):
    title = StringField('Session_id', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class EnterIdInfo(FlaskForm):
    title = StringField('Session_id', validators=[DataRequired()])
    title_p = StringField('Parameter', validators=[DataRequired()])
    submit = SubmitField('Submit')

    



    

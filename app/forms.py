from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QuestionairreForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    need_help = BooleanField('Need Help?')
    need_help_description = StringField('Describe Help', validators=[DataRequired()])
    provide_help = BooleanField('Providing Help?')
    provide_help_description = StringField('Describe Provide', validators=[DataRequired()])
    description_hashtags = StringField('Add Tags', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    #from tutorial
    # username = StringField('Username', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')

from flask import render_template
from app import app
from app.forms import QuestionairreForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('layout.html', title='Home', user=user)

@app.route('/questionnaire')
def getFormPostData():
    form = QuestionairreForm()
    return render_template('questionnaire_form.html', title='Sign In', form=form)
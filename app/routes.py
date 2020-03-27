from flask import render_template
from app import app
from app.forms import QuestionairreForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('layout.html', title='Home', user=user)

@app.route('/questionnaire', methods=['GET', 'POST'])
def getFormPostData():
    form = QuestionairreForm()
    if form.validate_on_submit():
        
        return render_template('questionnaire_form.html', title='Sign In', form=form)
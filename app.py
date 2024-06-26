from bpresources import get_sessions
from flask import Flask, render_template, make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import DateField, SubmitField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)

class MyForm(FlaskForm):
    date = DateField('Swim date', default=datetime.today())
    submit = SubmitField('Go')

@app.route('/', methods=['GET', 'POST'])
def index():
    swim_date = datetime.today()
    sessions = get_sessions(swim_date)
    form = MyForm()
    if form.validate_on_submit():
        swim_date = form.data['date']
        sessions = get_sessions(swim_date.strftime('%Y-%m-%d'))
#        for session in s:
#            start_time = session["starts_at"]["format_12_hour"]
#            spaces = session["spaces"]
    resp = make_response(render_template('index.html', form=form, data=sessions))
    resp.set_cookie('swimdate', swim_date.strftime('%Y-%m-%d'))
    return resp
#
if __name__ == '__main__':
    app.run(debug=True)


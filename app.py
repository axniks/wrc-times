from bpresources import get_sessions
from flask import Flask, render_template, make_response, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import DateField, SubmitField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)

class MyForm(FlaskForm):
    date = DateField('Swim date')
    submit = SubmitField('Go')

@app.route('/', methods=['GET', 'POST'])
def index():
    date_format = '%Y-%m-%d'
    swim_date_str = request.cookies.get('swim_date')
    if swim_date_str:
        swim_date = datetime.strptime(swim_date_str, date_format)
    else:
        swim_date = datetime.today()

    sessions = get_sessions(swim_date)
    form = MyForm()
    if form.validate_on_submit():
        swim_date = form.data['date']
        sessions = get_sessions(swim_date)

    resp = make_response(render_template('index.html', form=form, data={'sessions':sessions, 'swim_date':swim_date}))
    resp.set_cookie('swim_date', swim_date.strftime(date_format))
    return resp

if __name__ == '__main__':
    app.run(debug=True)


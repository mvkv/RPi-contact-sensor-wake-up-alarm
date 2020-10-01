from flask import Flask, render_template, request
from clock_checker import ClockChecker
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_components import TimeField
from flask_bootstrap import Bootstrap

# Initializing Flask app
app = Flask(__name__)
Bootstrap(app)

clock_checker = ClockChecker()  # Initializing thread that checks time

class Timeform(FlaskForm):  # HTML time field to retrieve data
    wake_up_time = TimeField('Waking up time: ')
    submit = SubmitField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Timeform()

    if request.method == 'POST':  # Gets data from form
        hours, minutes, seconds = str(form.wake_up_time.data).split(":")
        print(clock_checker.get_wakeup_hour())
        clock_checker.define_time(int(hours), int(minutes))  # Sets the time in the thread
    return render_template('index.html', form=form, wake_up_time=clock_checker.get_wakeup_hour())

@app.route('/stop')
def stop():
    clock_checker.stop_alarm()

@app.route('/start')
def start():
    clock_checker.start_alarm()


app.run(port=80, host="0.0.0.0", debug=True)

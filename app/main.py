import datetime
from flask import Flask
from flask import render_template, request, redirect

from config import Config
from form import BirthdayForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET", "POST"])
def index():
    form = BirthdayForm()
    if form.validate_on_submit():
        # return redirect('/ages', then=form.birthday.data)
        return ages(form.birthday.data)
    return render_template('index.html.jinja', title='Sign In', form=form)


@app.route("/ages", methods=["GET", "POST"])
def ages(then=str(datetime.datetime.now())):
    now = datetime.datetime.now()
    days = (now - then).days
    planets = {k: round(days/v, 2) for k, v in Config.planets.items()}
    return render_template('ages.html.jinja', planets=planets)


if __name__ == "__main":
    app.run()

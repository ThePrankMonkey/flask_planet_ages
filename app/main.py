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
        return render_template('index.html.jinja', title='Planet Birthdays', form=form, planets=ages(form.birthday.data))
    return render_template('index.html.jinja', title='Planet Birthdays', form=form, planets=False)


def ages(then=datetime.date.today()):
    print("Getting Ages")
    now = datetime.date.today()
    days = (now - then).days
    planets = {k: round(days/v, 2) for k, v in Config.planets.items()}
    return planets


if __name__ == "__main":
    app.run()

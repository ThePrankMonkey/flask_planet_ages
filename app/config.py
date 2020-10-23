import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    planets = {
        "Mercury": 87.97,
        "Venus": 224.7,
        "Earth": 365.25,
        "Mars": 686.67,
        "Jupiter": 4331.865,
        "Saturn": 10760.265,
        "Uranus": 30684.6525,
        "Neptune": 60189.5475,
        # "Pluto": 90797.4975,
    }

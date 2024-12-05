# application.py
from flask import Flask, request
from flask_babel import Babel, gettext

application = Flask(__name__)
babel = Babel(application)

LANGUAGES = {
    'en': 'Hello World!',
    'es': '¡Hola Mundo!',
    'fr': 'Bonjour le Monde!',
    'de': 'Hallo Welt!'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@application.route('/')
def hello():
    return LANGUAGES.get(get_locale(), LANGUAGES['en'])

if __name__ == '__main__':
    application.run()



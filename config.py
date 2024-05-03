from dotenv import load_dotenv
import os

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN = os.environ.get('TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')

    CATEGORIES = {
       "Кино🎞️":2,
       "Музыка🎻":4,
       "Видеоигры🕹️":15,
       "Живопись/арт 🖌️":5,
       "Общественная жизнь👥":6,
       "Театр🎭":7,
       "Литература📚":8,
       "Спорт⛹️":9,
       "Другое⚖️":10
    }
from dotenv import load_dotenv
import json
import os

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN = os.environ.get('TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')
    with open("categories.json", encoding="UTF-8") as f:
        CATEGORIES = json.load(f)

    def update_categories():
        with open("categories.json", "w", encoding="UTF-8") as f:
            json.dump(Config.CATEGORIES, f, ensure_ascii=False, indent=4)
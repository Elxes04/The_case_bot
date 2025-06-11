import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'thecasebot.conf'))

DA_TOKEN = config['bot']['DA_TOKEN']
CUSTOM_ID = config['custom']['CUSTOM_ID']
SPECIAL_MSG = config['custom']['SPECIAL_MSG']
BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, 'database')
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, 'the_casebot_database.db')
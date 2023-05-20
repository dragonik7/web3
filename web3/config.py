import os

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv('.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'
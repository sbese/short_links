import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
SITE_DOMAIN = os.environ.get('SITE_DOMAIN')
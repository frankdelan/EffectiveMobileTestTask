import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.environ.get('DATABASE_PATH')

from dotenv import load_dotenv
from os import getenv

load_dotenv()

YOUTUBE_API_KEY = getenv('YOUTUBE_API_KEY')
VK_LOGIN = getenv('VK_LOGIN')
VK_PASSWORD = getenv('VK_PASSWORD')
TG_TOKEN = getenv('TG_TOKEN')
NEWS_API_KEY = getenv('NEWS_API_KEY')
SITE = 'https://blog-flask-project.herokuapp.com'

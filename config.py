import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Twitter credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Telegram configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_NAME = os.getenv('TELEGRAM_CHANNEL_NAME')

# Search parameters
QUERY = "-filter:retweets"
THRESHOLD_DAYS = 1

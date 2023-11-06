import tweepy
import config
from datetime import datetime, timedelta
from telegram_bot import send_message

# Twitter API Authentication
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def is_account_fresh(created_at):
    return datetime.utcnow() - created_at < timedelta(days=config.THRESHOLD_DAYS)

def fetch_recent_accounts():
    for tweet in tweepy.Cursor(api.search_tweets, q=config.QUERY, result_type="recent").items(100):
        user = tweet.user
        if is_account_fresh(user.created_at):
            yield user

def run():
    try:
        for user in fetch_recent_accounts():
            message = (f"New account found: @{user.screen_name}, "
                       f"Created at: {user.created_at}, URL: {user.url if user.url else 'No URL'}, "
                       f"Followers: {user.followers_count}")
            send_message(message)
    except tweepy.TweepError as e:
        send_message(f"An error occurred: {e}")

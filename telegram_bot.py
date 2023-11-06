from telegram import Bot
import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

def send_message(message):
    bot.send_message(chat_id=config.TELEGRAM_CHANNEL_NAME, text=message)

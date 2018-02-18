import telegram
from telegram.ext import Updater, CommandHandler

from . import config


def send(chat_id, text):
    bot = telegram.Bot(token=config.BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=text)


def start():
    def cmdstart(bot, update):
        update.message.reply_text(
            'Your chat id {}'.format(update.message.chat_id))
    updater = Updater(config.BOT_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', cmdstart))
    updater.start_polling()
    updater.idle()

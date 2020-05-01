import telegram
from telegram.ext import Updater, CommandHandler

from . import config


def send(chat_id, text):
    if not chat_id or not text: return

    bot = telegram.Bot(token=config.BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=text)


def _cmdstart(update, context):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text='Your chat id {}'.format(chat_id))


def start():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', _cmdstart))
    updater.start_polling()
    updater.idle()

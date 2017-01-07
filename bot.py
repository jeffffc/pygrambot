import os
import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s - %(message)s')

token = os.environ.get('TOKEN')
appname = os.environ.get('APPNAME')
port = int(os.environ.get('PORT', '5000'))

updater = Updater(token)
updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(appname, token))


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')


def hello(bot, update):
    first_name = update.message.from_user.first_name
    update.message.reply_text('Hello {}'.format(first_name))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.idle()

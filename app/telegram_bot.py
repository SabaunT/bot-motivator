import os
import logging

from telegram.ext import Updater, CommandHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start(update, context):
    # todo move
    update.message.reply_text(text='SUP!')


class MotivatorBot:
    # todo assertions, better config handling
    # why use_context?
    def __init__(self):
        self.token = os.environ.get('BOT_TOKEN')
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def setup(self):
        start_handler = CommandHandler('start', start)

        self.dispatcher.add_handler(start_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, telegram_token: str):
        self._updater = Updater(telegram_token, use_context=True)
        self._dispatcher = self._updater.dispatcher
        self._bot = self._updater.bot
        self._callbacks = []
        self._dispatcher.add_handler(CallbackQueryHandler(self._callback))

    def add_entry_point(self, entry_point: str, function):
        self._dispatcher.add_handler(CommandHandler(entry_point, function))

    def run_bot(self):
        self._updater.start_polling()

    def send_msg_to_chat(self, chat_id: str, msg: str, accept: bool ):
        if accept:
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton('Yes', callback_data='True'),
                InlineKeyboardButton('No', callback_data='False')
            ]])
        else:
            reply_markup = None

        self._bot.send_message(text=msg, chat_id=chat_id, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

    def get_dispatcher(self):
        return self._dispatcher
    
    def get_callbacks(self):
        return self._callbacks
    
    def _callback(self, update, context):
        logger.info('_callback')
        response = update.callback_query.data
        update.callback_query.answer()
        update.callback_query.edit_message_reply_markup(reply_markup=None)
        self._callbacks.append(response)



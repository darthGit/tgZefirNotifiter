from telegram.ext import Updater, CommandHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


class Bot:
    def __init__(self, telegram_token: str):
        self._updater = Updater(telegram_token, use_context=True)
        self._dispatcher = self._updater.dispatcher
        self._bot = self._updater.bot

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



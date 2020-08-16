from bot import Bot
from telegram.ext import CallbackQueryHandler

def start(update, context):
    update.message.reply_text('hi from tg')
    bot.send_msg_to_chat('390499498','test msg with buttons', True)

def callback(update, context):
    response = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.edit_message_reply_markup(reply_markup=None)
    print(response)

bot = Bot('966337942:AAE0FiNCyhcR-nNMdGBn1bBqg0rGCw72t48')

bot.add_entry_point('start', start)

bot.run_bot()

bot.send_msg_to_chat('390499498','test msg with buttons', True)

bot.get_dispatcher().add_handler(CallbackQueryHandler(callback))

import asyncio
import time
import json
from bot import Bot
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceNotifiter():
    def __init__(self, bot: Bot, main_user: str):
        self._bot = bot
        self._main_user = main_user
        self._bot.add_entry_point('start', self._start)

    def send_msg(self, request):
        if request['type'] == 'REVIEW':
            accept = True
            msg = f"""*Message time is:* {request['datetime']}
            *Message:* {request['message']}
            *From:* {request['from']}
            """
        else:
            accept = False
            msg = f"""*Message time is:* {request['datetime']}
            *Message:* {request['message']}
            *From:* {request['from']}
            *Phone:* {request['phone']}
            *Email:* {request['email']}
            """

        self._bot.send_msg_to_chat(chat_id=self._main_user, msg=msg, accept=accept)

        if request['type'] != 'REVIEW':
            return dict(succes=True, chat_id=self._main_user)

        while not self._bot.get_callbacks():
            logger.info('in while')
            time.sleep(1)
            
        response = self._bot.get_callbacks().pop(0)

        return dict(succes=True, response=response)

    def _start(self,update, context):
        update.message.reply_text('Hi!')
        self._main_user = update.effective_user['id']
        logger.info(self._main_user)
        
    



import os
import logging
from flask import Flask, jsonify, abort
from flask import request
from bot import Bot
from tg_controlers import ServiceNotiter

app = Flask(__name__)
TG_NOTIFITER_TOKEN = os.getenv('TG_NOTIFITER_TOKEN')
bot = Bot(TG_NOTIFITER_TOKEN)
service = ServiceNotiter(bot)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    return 'ok', 200

@app.route('/shop/notification/api/v0.1/task', methods=['POST'])
def create_task():
    if not request.json or not 'token' in request.json:
        abort(400)
    requests = {
        'datetime': request.json['datetime'],
        'type': request.json['type'],
        'message': request.json['message'],
        'from': request.json['from'],
        'email': request.json['email'],
        'phone': request.json['phone']
    }
    
    response = service.send_msg(requests)

    return jsonify(response), 201

def main():
    bot.run_bot()
    app.run(host='0.0.0.0', port=80)
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    #updater.idle()


if __name__ == '__main__':
   main()

import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("bot_token")

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def getUpdates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset':offset}
        resp = requests.get(self.api_url+method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode':"HTML"}
        method = 'sendMessage'
        resp = requests.post(self.api_url+method, params)
        return resp

dhirajBot = BotHandler(token)

def main():
    new_offset = 0
    print('>> starting bot now!')

    while True:
        all_updates = dhirajBot.getUpdates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

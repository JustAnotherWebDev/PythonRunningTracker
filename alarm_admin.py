import requests
import json

json_file = open('../WebScrapVolleyball/util/security.json')
API_KEY = json.load(json_file)["telegram_token"]
json_file = open('../WebScrapVolleyball/util/security.json')
CHAT_ID = json.load(json_file)["dev_chatid"]

def telegram_bot_sendtext():
  bot_message = 'The BeachVolleyBall-Scanner came to a halt! Do something...'
  send_text = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={bot_message}'
  response = requests.get(send_text)
  return response.json()
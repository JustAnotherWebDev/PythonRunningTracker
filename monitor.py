import psutil
from alarm_admin import telegram_bot_sendtext

process_name = ""

run = true

while run == true:
  list = []
  for process in psutil.process_iter():
    list.append(process.name())
  if process_name not in list:
    telegram_bot_sendtext()
    run = false



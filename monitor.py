import psutil
from alarm_admin import telegram_bot_sendtext
import time
import datetime

run = True #hier auf true setzen, damit das Programm läuft!
print('Monitor of BeachVolleyBall-Scanner was started...')
counter = 0
while run == True:
  time.sleep(60)
  process_found = False
  for pid in psutil.pids():
    p = psutil.Process(pid)
    try:
      if p.cmdline()[1] == 'src/app.py':
        process_found = True
        counter = 0
        print('Program still running at: ', datetime.datetime.now().time.strftime('%Y-%m-%d %H:%M:%S'))
    except IndexError:
      counter += 1

      pass # Not every pid-Stream hast more than 1 Array-Element  
  if counter > 10:
    telegram_bot_sendtext()
    time.sleep(3600)
    telegram_bot_sendtext()
    time.sleep(7200)
    telegram_bot_sendtext()
    run = False
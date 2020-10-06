import psutil
from alarm_admin import telegram_bot_sendtext
import time

run = True #hier auf true setzen, damit das Programm läuft!
print('Monitor of BeachVolleyBall-Scanner was started...')
while run == True:
  #time.sleep(60)
  process_found = False
  for pid in psutil.pids():
    p = psutil.Process(pid)
    try:
      if p.cmdline()[1] == 'src/app.py':
        process_found = True
        print()
    except IndexError:
      pass # Not every pid-Stream hast more than 1 Array-Element  
  if process_found == False:
    telegram_bot_sendtext()
    time.sleep(3600)
    telegram_bot_sendtext()
    time.sleep(7200)
    telegram_bot_sendtext()
    run = False
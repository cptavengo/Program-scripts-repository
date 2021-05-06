#! /usr/bin/env python3

import schedule
import time

running = True
get_time = str(input("What time do you want to set an alarm for? "))

def job():
  global running
  running = False
  current_time = time.localtime()
  print("This is an alarm for {}:{}".format(current_time[3], current_time[4]))
  return schedule.CancelJob

schedule.every().day.at(get_time).do(job)

while running:
  schedule.run_pending()
  time.sleep(1)

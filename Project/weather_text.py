import schedule
import json
import requests

def hello():
    print("Hello")

schedule.every(5).seconds.do(hello)

while True:
    schedule.run_pending()

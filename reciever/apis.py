import requests
import json
from datetime import datetime
import time

def get_alarms():
    try:
        response = requests.get("http://localhost:8000/api/alarm-list/")
    except requests.ConnectionError as e:
        print (e)
        return [{"id": 2, "title": "test", "time": "15:45:58", "added_at": "2022-03-23T06:30:00+02:00"}]
    parsed = response.json()
    return parsed
def save_to_file():
    with open('reciever/alarms_data.json', 'w') as outfile:
        print("fetched")
        alarms_json = (get_alarms())
        json.dump(alarms_json, outfile)
    
def loop_for_checks_of_time():
    while(1):
        time.sleep(1)
        now = datetime.now()
        if(now.minute%5==0 and now.second==0):
        #if(now.second%5==0):
            save_to_file()
        #exit()
         
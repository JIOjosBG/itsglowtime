import requests
import json
from datetime import datetime
import time

def get_alarms():
    try:
        response = requests.get("http://172.104.240.173/api/alarm-list/")
    except requests.ConnectionError as e:
        print (e)
        return [{"id": 0, "title": "morning", "time": "7:00:00", "added_at": "2022-01-01T00:00:00+02:00"}]
    parsed = response.json()
    return parsed
def save_to_file():
    with open('/home/pi/Documents/itsglowtime/reciever/alarms_data.json', 'w') as outfile:
        print("fetched")
        alarms_json = (get_alarms())
        json.dump(alarms_json, outfile)
    
def loop_for_checks_of_time():
    while(1):
        try:
            time.sleep(1)
            now = datetime.now()
            if(now.minute%5==0 and now.second==0):
            #if(now.second%5==0):
                save_to_file()
            #exit()
        except Exception as e: print(e)         

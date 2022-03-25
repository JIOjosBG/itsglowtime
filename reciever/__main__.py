import hardware
import apis
from datetime import datetime
import threading
import json
import time

def get_next_alarm():
    with open('reciever/alarms_data.json', 'r') as f:
        data = json.load(f)[0]
    return data

def main():
    
    api_fetcher = threading.Thread(target=apis.loop_for_checks_of_time, args=())
    api_fetcher.start()
    time.sleep(1)
    print("asd")
    next_alarm = get_next_alarm()
    
    hardware_update = threading.Thread(target=hardware.digital_clock_lights, args=(next_alarm['time'],))
    hardware_update.start()
    
        
    #api_fetcher.join()



    return 1
    




if __name__ == "__main__":
    main()

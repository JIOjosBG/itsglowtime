import hardware
import apis
from datetime import datetime
import threading
import json
def get_next_alarm():
    with open('alarms_data.json', 'r') as f:
        data = json.load(f)[0]
    return data

def main():
    api_fetcher = threading.Thread(target=apis.loop_for_checks_of_time, args=())
    api_fetcher.start()
    while(1):
        # x = threading.Thread(target=thread_function, args=(1,))
        # time.sleep(1)
        # now = datetime.now()
        # if(now.second == 0 and now.minute%5==0):
        #     apis.save_to_file()

        next_alarm = get_next_alarm()

        hardware_update = threading.Thread(target=hardware.digital_clock_lights, args=(next_alarm['time'],))
        hardware_update.start()
        
    #api_fetcher.join()



    
    




if __name__ == "__main__":
    main()

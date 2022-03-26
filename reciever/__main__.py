import hardware
import apis
from datetime import datetime
import threading
import json
import time
def main():
    
    api_fetcher = threading.Thread(target=apis.loop_for_checks_of_time, args=())
    api_fetcher.start()
    time.sleep(1)
    
    hardware_update = threading.Thread(target=hardware.main_hardware_loop, args=())
    hardware_update.start()
    
        
    #api_fetcher.join()



    return 1
    




if __name__ == "__main__":
    main()

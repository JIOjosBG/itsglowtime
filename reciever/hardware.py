#ws2812 work here
import time
from datetime import datetime
import json
def main_hardware_loop():
    while(1):
        time.sleep(5)
        now = datetime.now()
        next_alarm=get_next_alarm()
        #if(next_alarm.minute==now.minute and next_alarm.hour == now.hour):
        if 1: #proverka dali e vreme za alarma
            display_time(now)


def display_time(t):
    print(t)


def get_next_alarm():
    with open('reciever/alarms_data.json', 'r') as f:
        data = json.load(f)[0]
    return data

    
def clock_loop():

    time.sleep(1)
    t = datetime.now()
    #segments_to_index(t[0:2]+t[3:5])

    exit()


nums_as_7_segment = [
    [1,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    [1,1,0,1,1,0,1],
    [1,1,1,1,0,0,1],
    [0,1,1,0,0,1,1],
    [1,0,1,1,0,1,1],
    [1,0,1,1,1,1,1],
    [1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1],
]


def index_to_2d(x,y,l,h,offset=0):
    if(y%2==0):
        return y*l+x+offset
    else:
        return y*l+(l-x-1)+offset


# 0   1   2   3   4
# 9   8   7   6   5
# 10  11  12  13  14
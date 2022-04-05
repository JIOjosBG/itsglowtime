#ws2812 work here
import time
from datetime import datetime
import json
import board
import neopixel

def main_hardware_loop():
    while(1):
        time.sleep(5)
        now = datetime.now()
        next_alarm=get_next_alarm()
        #if(next_alarm.minute==now.minute and next_alarm.hour == now.hour):
        if 1: #proverka dali e vreme za alarma
            display_time(now)


def display_time(t):
    t_as_string = str(t)[11:13]+str(t)[14:16]
    nums_as_grids = get_nums_as_grids(t_as_string)
    # for i in nums_as_grids:
    #     print('\n')
    #     for j in i:
    #         print(j)
    final_indexes=[]
    final_indexes+=(get_indexes_from_grid(nums_as_grids[0],0))
    final_indexes+=(get_indexes_from_grid(nums_as_grids[1],5))
    final_indexes+=(get_indexes_from_grid(nums_as_grids[2],12))
    final_indexes+=(get_indexes_from_grid(nums_as_grids[3],17))
    indexes_to_ws2812(final_indexes)


def indexes_to_ws2812(indexes):
    pixel_pin = board.D18
    num_pixels = 150
    ORDER = neopixel.GRB

    pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1)
    while(1):
        for j in indexes:
            pixels[j]=[255,255,255]
        pixels.show()
        time.sleep(1)
        pixels.fill((0,0,0))
        time.sleep(1)

def get_indexes_from_grid(grid,offset):
    indexes=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]==1):
                indexes.append(index_to_2d(j+offset,i,21,7,3))

    return indexes

def get_nums_as_grids(t):
    nums_as_grids = []
    #print(t)
    for n in t:
        nums_as_grids.append(get_num_as_grid(int(n)))
    return nums_as_grids

def get_num_as_grid(n):
    grid=[]
    for i in range(7):
        grid.append([0,0,0,0])
    current_num_as_7_segment = nums_as_7_segment[n]

    for i in range(len(current_num_as_7_segment)):
        if current_num_as_7_segment[i]==1:
            if i==0:
                for j in range(4):
                    grid[0][j]=1
            elif i==1:
                for j in range(4):
                    grid[j][3]=1
            elif i==2:
                for j in range(4):
                    grid[j+3][3]=1
            elif i==3:
                for j in range(4):
                    grid[6][j]=1
            elif i==4:
                for j in range(4):
                    grid[j+3][0]=1
            elif i==5:
                for j in range(4):
                    grid[j][0]=1
            elif i==6:
                for j in range(4):
                    grid[3][j]=1

    return grid

def get_next_alarm():
    with open('~/Documents/itsglowtime/reciever/alarms_data.json', 'r') as f:
        data = json.load(f)[0]
        #da se napravi da e pyrvata sledvashta a ne prosto pyrvata
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
    [1,1,1,1,0,1,1],
]


def index_to_2d(x,y,l,h,offset=0):
    if(y%2==0):
        return y*l+x+offset
    else:
        return y*l+(l-x-1)+offset


# 0   1   2   3   4
# 9   8   7   6   5
# 10  11  12  13  14

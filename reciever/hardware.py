#ws2812 work here
import time
def digital_clock_lights(t):
    #print("set lights")
    
    time.sleep(1)
    for i in range(21):
        for j in range(7):
            pass
          #print(index_to_2d(i,j,21,7,3))  
    #print(index_to_2d(0,1,21,7,3))
    #print(t[3:5])
    exit()


nums = [
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
import requests 


url = 'http://172.104.240.173/api/alarm-create/'
myobj = {
        "title": "python",
        "time": "20:25:00",
        "red": 24,
        "green": 100,
        "blue": 45
}
x = requests.post(url, data =myobj)
print(x.__dir__())
print(x.reason)
print(x.status_code)
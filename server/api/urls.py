from django.urls import path

from .views import alarmList, alarmNext, apiOverview

urlpatterns = [
    # ex: /polls/
    path('', apiOverview, name='list-api'),
    path('alarm-list/', alarmList, name='list-alarms'),
    path('alarm-next/', alarmNext, name='next-alarm'),
]
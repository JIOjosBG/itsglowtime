from django.urls import path

from .views import alarmList, apiOverview

urlpatterns = [
    # ex: /polls/
    path('', apiOverview, name='list-api'),
    path('alarm-list/', alarmList, name='list-alarms'),
]
from django.urls import path

from .views import alarmList, alarmNext, apiOverview, alarmCreate, alarmDelete

urlpatterns = [
    # ex: /polls/
    path('', apiOverview, name='list-api'),
    path('alarm-list/', alarmList, name='list-alarms'),
    path('alarm-next/', alarmNext, name='next-alarm'),
    path('alarm-create/', alarmCreate, name='create-alarm'),
    path('alarm-delete/<str:pk>', alarmDelete, name='delete-alarm'),
]
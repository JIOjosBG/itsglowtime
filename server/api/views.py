from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from datetime import datetime, time
from django.utils import timezone

from .serializers import AlarmSerializer
from .models import Alarm

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/alarm-list/',
        'Next': '/alarm-next/',
        'Create': '/alarm-create/',
        'Delete': '/alarm-delete/<pk>',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def alarmList(request):
    alarms = Alarm.objects.all().order_by('time')
    serializer = AlarmSerializer(alarms,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def alarmNext(request):
    midnight = time(23,59,59)
    alarm = Alarm.objects.filter(time__range=(datetime.now(),midnight)).order_by('time').first()
    print(datetime.now())
    serializer = AlarmSerializer(alarm,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def alarmCreate(request):
    serializer = AlarmSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print(request.data)
    #serializer = AlarmSerializer(alarm,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def alarmDelete(request,pk):
    alarm = Alarm.objects.get(id=pk)
    alarm.delete()
    print("watafak")

    return Response("deleted")
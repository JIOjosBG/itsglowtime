from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from datetime import datetime
from django.utils import timezone

from .serializers import AlarmSerializer
from .models import Alarm

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/alarm-list/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def alarmList(request):
    alarms = Alarm.objects.all()
    serializer = AlarmSerializer(alarms,many=True)
    return Response(serializer.data)

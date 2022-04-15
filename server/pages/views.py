from django.shortcuts import render
# Create your views here.
from .forms import AlarmForm
from api.models import Alarm
def homepage(request):
    form = AlarmForm()
    #return HttpResponse("asdasd")
    if request.method == "POST":
        form = AlarmForm(request.POST)
        if form.is_valid:
            form.save()

        form = AlarmForm()
    alarms = Alarm.objects.all()
    context={'form':form,"alarms":alarms}

    return render(request,'index.html',context)
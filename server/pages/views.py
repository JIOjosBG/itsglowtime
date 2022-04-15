from django.shortcuts import render
# Create your views here.
from .forms import AlarmForm

def homepage(request):
    form = AlarmForm()
    #return HttpResponse("asdasd")
    if request.method == "POST":
        form = AlarmForm(request.POST)
        if form.is_valid:
            form.save()

        form = AlarmForm()

    context={'form':form}

    return render(request,'index.html',context)
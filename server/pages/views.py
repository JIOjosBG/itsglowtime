from django.shortcuts import render
# Create your views here.

def homepage(request):
    #return HttpResponse("asdasd")
    return render(request,'index.html')
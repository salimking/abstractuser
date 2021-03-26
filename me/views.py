from django.shortcuts import render,HttpResponse
from . form import Customesign
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    f=Customesign()
    if request.method=="POST":
        f=Customesign(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("saved")
    con={
        'f':f
    }
    return render(request,'index.html',con)

def ulog(request):
    
    if request.method=="POST":
        
        u=request.POST['name']
        p=request.POST['passw']
        o=authenticate(request,users=u,passw=p)
        if o is not None:
            login(request,o)
            return HttpResponse("You are Coustomer")
             
    return render(request,'log.html')
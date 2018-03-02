from django.shortcuts import render,HttpResponse
from core.hostInfo import *
from core.autopack import *
# Create your views here.

def index(requests):
    if requests.method=='GET':
        title='Default Index Page'
        c=cpuInfo()
        m=memInfo()
        boot=bootInfo()
        huser=userInfo()
        return render(requests,'update/hostInfo.html',locals())
    if requests.method=='POST':
        pass

def jenkins(requests):
    Jview=Jviews()
    title='jenkins'
    # print(jobname)
    return render(requests,'update/jenkins.html',locals())
def jenkins2(requests,jobname):
    Jview=Jviews()
    title='jenkins'
    print(jobname)
    return render(requests,'update/jenkins.html',locals())
def add2(request, a, b):
    c = int(a) + int(b)
    print(a,b)
    return HttpResponse(str(c))
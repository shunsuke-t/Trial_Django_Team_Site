from django.shortcuts import render,HttpResponse

def index(req):
    return render(req,'top/index.html')
#    return HttpResponse("Hello!")


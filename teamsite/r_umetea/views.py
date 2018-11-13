from django.http import HttpResponse

def index(request):
    return HttpResponse("umetea room")
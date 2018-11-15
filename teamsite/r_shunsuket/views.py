from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def main(req):
    return HttpResponse("メインページだお")

def front(req):
    return HttpResponse("ここはフロントページです")

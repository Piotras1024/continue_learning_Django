from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome_page(request):
    return HttpResponse('Welcome')


def date(request):
    return HttpResponse('This paged was served at : ' + str(datetime.now()))


def about(request):
    return HttpResponse('Hej, I am Peter Dabrowski, the YOLO style PLAYER')


# Create your views here.

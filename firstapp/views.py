from django.shortcuts import render
from django.http import HttpResponse
import datetime
def display(request):
    return HttpResponse('<h1> Hello World </h1>')

def date_time(request):
    date=datetime.datetime.now()
    s='<h1> The current date and time at server is: '+str(date)+'</h1>'
    return HttpResponse(s)

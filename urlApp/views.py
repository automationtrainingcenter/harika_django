from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello URLs</h1>')


def get_time(request, hours=0):
    hours = int(hours)
    if hours == 0:
        dt = datetime.now()
        return HttpResponse(f'<h1>Time is {dt}</h1>')
    else:
        dt = datetime.now() + timedelta(hours=hours)
        return HttpResponse(f'<h1>Time after {hours} hours is {dt}')


def get_id(request, id):
    return HttpResponse(f'<h1>Hi your id is {id}</h1>')


def get_user(request, username):
    return HttpResponse(f'<h1>Hello {username}</h1>')

def get_user_details(request, username, id, email):
    return HttpResponse(f'<h1>Hello {username} your id is {id} and emai is {email}')

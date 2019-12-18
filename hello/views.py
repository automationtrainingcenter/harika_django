from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world!! from hello app<h1>")

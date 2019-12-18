from django.shortcuts import render

# Create your views here.


def template_home(request):
    return render(request, 'templateApp/home.html')


def template_data(request):
    # sending data from view to html
    return render(request, 'templateApp/data.html', {'name': 'Harika'})

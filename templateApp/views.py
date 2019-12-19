from django.shortcuts import render

# Create your views here.


def template_home(request):
    return render(request, 'templateApp/home.html')


def template_data(request):
    # sending data from view to html
    return render(request, 'templateApp/data.html', {'name': 'Harika'})


def more_on_template_data(request):
    context = {
        'is_valid': True,
        'name': 'surya',
        'phone_num': '9876543210',
        'courses': ['c', 'cpp', 'java', 'python', 'django', 'flask', 'selenium', 'testing']
    }
    return render(request, 'templateApp/more_data.html', context)

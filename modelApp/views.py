from django.shortcuts import render
from modelApp.models import Programmer, Project

# Create your views here.


def programmer_list(request):
    programmers = Programmer.objects.all()
    return render(request, "modelApp/programmers.html", {'programmers': programmers})


def project_info(request, name):
    pro = Project.objects.get(name=name)
    programmers = pro.programmer_set.all()
    return render(request, 'modelApp/programmers.html', {'programmers': programmers})

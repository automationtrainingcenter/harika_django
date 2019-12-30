
from django.shortcuts import render

# Create your views here.


def html_form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST['email']
        phone_number = request.POST.get('phnum')
        print(f'{fullname}\n{email}\n{phone_number}')
    return render(request, 'formsApp/html_form.html')

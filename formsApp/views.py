
from django.shortcuts import render
from formsApp.forms import ContactForm, ProjectForm

# Create your views here.


def html_form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST['email']
        phone_number = request.POST.get('phnum')
        print(f'{fullname}\n{email}\n{phone_number}')
    return render(request, 'formsApp/html_form.html')


def django_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['fullname'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['content'])
    else:
        form = ContactForm()
    return render(request, 'formsApp/django_form.html', {'form': form})


def model_form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ProjectForm()
    return render(request, 'formsApp/model_form.html', {'form': form})

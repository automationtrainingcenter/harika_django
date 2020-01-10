from django.shortcuts import render
from sessionApp.forms import ProductForm

# Create your views here.


def index(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    return render(request, 'sessionApp/index.html', {'count': count})


def products_page(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            quantity = form.cleaned_data.get('quantity')
            request.session[name] = quantity
            form = ProductForm()
    return render(request, 'sessionApp/products.html', {'form': form})


def cart_page(request):
    return render(request, 'sessionApp/cart.html')

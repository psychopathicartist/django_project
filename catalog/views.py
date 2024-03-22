from django.shortcuts import render
from catalog.models import Product


def home(request):
    context = {'object_list': Product.objects.all()}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'''Имя: {name}
Номер телефона: {phone}
Сообщение: {message}''')

    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'catalog/product.html', context)

from django.shortcuts import render
from .import models


# Create your views here.
def homepage(request):
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()

    # Получим значение введенное в поисковой строке сайта
    from_frontend = request.GET.get('exact_product')

    # Было ли введено что-то в поиске
    if from_frontend is not None:
        all_products = models.Product.objects.filter(product_name__contains=from_frontend)

    context = {'all_categories': all_categories, 'products': all_products}

    return render(request, 'index.html', context)


# Получить определенный продукт
def exact_product(request, pk):
    find_product_from_db = models.Product.objects.get(id=pk)

    context = {'product': find_product_from_db}

    return render(request, 'exact_product.html', context)


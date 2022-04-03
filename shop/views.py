from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    products_objects = Products.objects.all()

    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        products_objects = products_objects.filter(product_name__icontains=product_name)

    paginator = Paginator(products_objects, 3)
    page = request.GET.get('page')
    products_objects = paginator.get_page(page)

    return render(request, 'index.html', {'products_objects': products_objects})


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'detail.html', {'product_object': product_object})

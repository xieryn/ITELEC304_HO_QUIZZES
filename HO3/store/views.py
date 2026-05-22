from django.shortcuts import render

from django.shortcuts import render
from .models import Product


def product_list(request):
    all_products = Product.objects.all()

    context = {"all_products": all_products}

    return render(request, "store/product_list.html", context)

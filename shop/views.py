from django.shortcuts import render, get_object_or_404
from products.models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, active=True)
    return render(request, 'products/product/detail.html', {'product': product})
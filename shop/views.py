from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from cart.forms import CartAddProductForm

"""
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_by_category = {}
    for category in categories:
        products = Product.objects.filter(category=category)
        products_by_category[category] = products
    products_by_category = products_by_category.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_by_category = products_by_category.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'categories': categories,
                   'products_by_category': products_by_category})
                """


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_active=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

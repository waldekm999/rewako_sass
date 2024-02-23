from django.shortcuts import render, get_object_or_404
from products.models import Product, Category



def product_list(request):
    categories = Category.objects.all()
    products_by_category = {}
    for category in categories:
        products = Product.objects.filter(category=category)
       #print(f"Category: {category.name}, Products: {products}")  # Debug print
        products_by_category[category] = products
    #print(f"Products by category: {products_by_category}")  # Debug print
    return render(request, 'shop/product/list.html', {'categories': categories, 'products_by_category': products_by_category})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_active=True)
    return render(request, 'shop/product/detail.html', {'product': product})

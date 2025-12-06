from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# 1. Главная страница: показывает все товары и список категорий
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all() 
    return render(request, 'my_shop/product_list.html', {
        'products': products, 
        'categories': categories
    })

# 2. Страница категории: показывает товары только ОДНОЙ категории
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category) 
    categories = Category.objects.all() 
    
    return render(request, 'my_shop/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category 
    })
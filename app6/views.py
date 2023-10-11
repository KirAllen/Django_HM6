from django.shortcuts import render

from django.db.models import Sum

from app5.models import Product

def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'All amount in DB',
        'total': total,
    }
    return render(request, 'app6/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Total in View',
        'total': total,
    }
    return render(request, 'app6/total_count.html', context)

def total_in_template(request):
    context = {
        'title': 'Total in template',
        'products': Product,
    }
    return render(request, 'app6/total_count.html', context)

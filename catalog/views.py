from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

from django.db.models import Q
# Create your views here.

def product_list(request):
    product_search = request.GET.get('search', '')
    if product_search:
        product = Product.objects.filter(Q(name__icontains = product_search) | Q(description__icontains = product_search))
    else:
        product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product':product,
        'category':category,
    }
    return render(request,'index.html', context)

def product_detail(request, slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id 
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    product = Product.objects.get(slug=slug)
    context = {
        'product':product,
        'cart': cart,
    }
    return render(request,'detail.html', context)

def category_detail(request, slug):
    category_self = Category.objects.get(slug=slug)
    category = Category.objects.all()
    mark = Mark.objects.filter(category = category_self)
    #product = Product.objects.filter(mark = mark_self)
    context = {
        'category_self':category_self,
        'category':category,
        #'product':product,
        'mark':mark,
    }
    return render(request,'category_detail.html', context)

def mark_detail(request, slug):
    mark_self = Mark.objects.get(slug=slug)
    category = Category.objects.all()
    product = Product.objects.filter(mark = mark_self)
    context = {
        'mark_self':mark_self,
        'category':category,
        'product':product,
    }
    return render(request,'mark_detail.html', context)

def cart_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id 
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    context = {
        'cart':cart,
    }
    return render(request, 'cart.html', context)

def add_to_cart_view(request, slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id 
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    product = Product.objects.get(slug=slug)
    new_item , _ = CartItem.objects.get_or_create(product = product, item_total=product.price)
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
    return HttpResponseRedirect('/catalog/cart/')

    
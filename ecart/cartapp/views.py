from django.shortcuts import render, redirect, get_object_or_404
from ecartapp.models import product
from .models import Cart,Cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart.request.session.create()
    return cart

def add_cart(request,product_id):
    products=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cartid=_cart_id(request))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cartid=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item = Cartitem.objects.get(products=products,cart=cart)
        if cart_item.quantity <=cart_item.products.stock:
            cart_item.quantity += 1
        cart_item.save(),
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            products=products,
            quantity=1,
            cart=cart
        )
        cart_item.save(),
    return redirect('cartapp:cartdetail')
def cartdetail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cartid=_cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)
        for i in cart_items:
            total +=(i.products.price*i.quantity)
            counter += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cartremove(request,product_id):
    cart = Cart.objects.get(cartid=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_items = Cartitem.objects.get(products=products,cart=cart)
    if cart_items.quantity >1:
        cart_items.quantity -=1
        cart_items.save(),
    else:
        cart_items.delete()
    return redirect('cartapp:cartdetail')

def cartdelete(request,product_id):
    cart = Cart.objects.get(cartid=_cart_id(request))
    products = get_object_or_404(product, id=product_id)
    cart_items = Cartitem.objects.get(products=products, cart=cart)
    cart_items.delete()
    return redirect('cartapp:cartdetail')
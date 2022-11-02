from .models import Cart,Cartitem
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cartid=_cart_id(request))
            cart_items=Cartitem.objects.filter(cart=cart[:1])
            for i in cart_items:
                item_count += i.quantity
        except Cart.DoesNotExist :
            item_count=0
        return dict(item_count=item_count)
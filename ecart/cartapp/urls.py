from . import views
from django.urls import path
app_name='cartapp'
urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('/',views.cartdetail,name='cartdetail'),
    path('remove/<int:product_id>/',views.cartremove,name='cartremove'),
    path('delete/<int:product_id>/',views.cartdelete,name='cartdelete'),
]
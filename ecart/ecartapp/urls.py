from . import views
from django.urls import path
app_name='ecartapp'
urlpatterns = [
    path('',views.allProdcat,name='allProdcat'),
    path('<slug:c_slug>/',views.allProdcat,name='products_by_category'),
    path('<slug:c_slug>/,<slug:product_slug>/',views.proddetail,name='productsdetail'),
]
from django.db import models
from ecartapp.models import product
# Create your models here.
class Cart(models.Model):
    cartid=models.CharField(max_length=250,blank=True)
    dateadded=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['dateadded']
    def __str__(self):
        return self.cartid
class Cartitem(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class  Meta:
        db_table='Cartitem'
    def sub_total(self):
        return self.products.price * self.quantity
    def __str__(self):
        return '{}'.format(self.products)
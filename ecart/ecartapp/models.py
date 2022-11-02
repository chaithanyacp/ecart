from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    desc=models.TextField()
    image=models.ImageField(upload_to='categoryimg',blank=True)
    slug=models.SlugField(max_length=255,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('ecartapp:products_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='productimg',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    slug=models.SlugField(max_length=255,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def get_url(self):
        return reverse('ecartapp:productsdetail',args=[self.category.slug,self.slug])

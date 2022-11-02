from django.contrib import admin

# Register your models here.
from.models import Category,product
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':['name',]}
admin.site.register(Category,Categoryadmin)
class Productadmin(admin.ModelAdmin):
    list_display = ['name','slug','created','updated','stock','available','price']
    list_editable = ['stock','price','available']
    prepopulated_fields = {'slug': ['name', ]}
    list_per_page = 20
admin.site.register(product,Productadmin)
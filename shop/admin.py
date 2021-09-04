from django.contrib import admin
from .models import Product,Contact
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","desc","pub_date")

admin.site.register(Product,ProductAdmin)

admin.site.register(Contact)
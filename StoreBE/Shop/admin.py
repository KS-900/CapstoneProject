from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

@admin.register(models.Product)
class PoductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status']
    list_display_links = ['title']
    list_editable = ['price']
    search_fields = ['title']
    list_filter = ['price']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'orders']
    list_editable = ['phone']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']

    @admin.display(ordering='orders')
    def orders(self, customer):
        url = (reverse('admin:Shop_order_changelist')
               + '?'
               + urlencode({
                   'order__id': str(customer.id)
               }))
        return format_html('<a href = "{}">{}</a>',url, customer.orders)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders=Count('order')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','payment_status', 'customer']
    list_editable = ['payment_status']
    search_fields = ['customer']
    list_filter = ['payment_status', 'placed_at']
    

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
                reverse('admin:Shop_product_changelist')
               + '?'
               + urlencode({
                   'collection__id': str(collection.id)
               }))
        return format_html('<a href = "{}">{}</a>',url, collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
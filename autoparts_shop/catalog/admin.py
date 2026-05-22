from django.contrib import admin
from .models import Brand, Part

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    search_fields = ['name']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'brand', 'category', 'price', 'stock', 'is_active']
    list_filter = ['brand', 'category', 'is_active']
    search_fields = ['article', 'name']
    list_editable = ['price', 'stock', 'is_active']
    fieldsets = (
        ('Основное', {
            'fields': ('article', 'name', 'description', 'category', 'brand')
        }),
        ('Цены и наличие', {
            'fields': ('price', 'stock')
        }),
        ('Дополнительно', {
            'fields': ('image', 'compatibility', 'is_active')
        }),
    )
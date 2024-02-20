from django.contrib import admin

from django.contrib import admin
from .models import Product, Category



# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    settings_fields = ('name', 'slug')
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class StripeAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'price', 'tax', 'category', 'is_active')
    list_filter = ('category', 'tax', 'width', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ('name',)


"""

@admin.register(Stripe)
class StripeAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'thickness', 'special_description', 'colour', 'price', 'isCool', 'ribbed')
    list_filter = ('width', 'thickness', 'colour', 'isCool', 'ribbed')
    search_fields = ('name', 'special_description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'updated'
    ordering = ('width', 'colour')


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'material', 'price')
    list_filter = ('width', 'material')
    search_fields = ('name', 'material')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'updated'
    ordering = ('width', 'material')


@admin.register(Hanger)
class HangerAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'material', 'price')
    list_filter = ('length', 'material')
    search_fields = ('name', 'material')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'updated'
    ordering = ('length', 'material')
    
    """

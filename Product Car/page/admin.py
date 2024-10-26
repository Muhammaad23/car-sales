from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_percent', 'is_active', 'county')  # Fields to display in the admin list
    list_filter = ('is_active', 'discount_percent')  # Filters for the sidebar
    search_fields = ('title', 'description')  # Searchable fields

    # Optionally, set the fields to be displayed in the form in a specific order
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'discount_percent', 'county', 'is_active')
        }),
        ('Image', {
            'fields': ('image',),
            'classes': ('collapse',),  # Collapse image fieldset
        }),
    )

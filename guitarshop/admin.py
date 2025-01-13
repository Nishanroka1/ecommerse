# guitar_shop/admin.py
from django.contrib import admin
from .models import Guitar

@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

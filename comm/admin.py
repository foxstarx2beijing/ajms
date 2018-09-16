from django.contrib import admin
from .models import color_info

@admin.register(color_info)
class color_infoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'color_code', 'description')
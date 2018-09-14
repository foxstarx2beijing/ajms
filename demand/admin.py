from django.contrib import admin
from .models import human, demand

class humanAdmin(admin.ModelAdmin):
    empty_value_display = '- empty -'
    list_display = ('name', 'company', 'deparment', 'phone', 'email')

admin.site.register(human, humanAdmin)
admin.site.register(demand)

from django.contrib import admin
from .models import human, demand

class humanAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'human_type', 'company', 'deparment', 'title', 'phone', 'email')
    list_per_page = 20
    fieldsets = (
        ['个人信息', {
            'fields': ('name', 'human_type')
        }], 
        ['公司信息', {
            'fields': ('company', 'deparment', 'title')
        }], 
        ['联系信息', {
            'fields': ('phone', 'email')
        }]
    )

admin.site.register(human, humanAdmin)
admin.site.register(demand)

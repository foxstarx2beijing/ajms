from django.contrib import admin
from .models import human, demand

class humanAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'human_type', 'company', 'deparment', 'title', 'phone', 'email')
    # list_display = ('name', 'get_human_type_display', 'shortname', 'phone', 'email')
    list_per_page = 20
    list_filter = ('company', 'deparment')
    search_fields = ('name', 'human_type', 'company', 'deparment', 'title', 'phone', 'email')
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

class demandAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'publisher', 'publish_date', 'priority', 'processor', 'percent', 'status')
    list_per_page = 20
    # fieldsets = ('name', 'publisher', 'publish_date', 'priority', 'processor', 'percent')
    fieldsets = (
        [
            '基本信息', {
                'fields': ('name', 'publisher', 'priority', 'processor', 'percent', 'status')
            }
        ], 
        [
            '详细信息', {
                'fields': ('description',)
            }
        ], 
    )

admin.site.register(human, humanAdmin)
# admin.site.register(processor, humanAdmin)
admin.site.register(demand, demandAdmin)

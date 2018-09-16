from django.contrib import admin
from .models import human_type, human, demand, demand_status

@admin.register(human_type)
class human_typeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'color_code', 'description')
    list_editable = ['color_code']

@admin.register(human)
class humanAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'colored_human_type', 'shortname', 'phone', 'email')
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

@admin.register(demand)
class demandAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'publish_date', 'status', 'publisher', 'publish_date', 'priority', 'processor', 'percent')
    list_per_page = 20
    # fieldsets = ('name', 'publisher', 'publish_date', 'priority', 'processor', 'percent')
    fieldsets = (
        [
            '基本信息', {
                'fields': (('name', 'priority'), ('publisher', 'processor'), 'percent', 'status')
            }
        ], 
        [
            '详细信息', {
                'fields': ('description',)
            }
        ], 
    )
    list_editable = ['status', 'percent']
    date_hierarchy = 'publish_date'

@admin.register(demand_status)
class demand_statusAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'description')
    

admin.site.site_header = 'Asiainfo Job Managment System'
admin.site.site_title = 'AJMS'
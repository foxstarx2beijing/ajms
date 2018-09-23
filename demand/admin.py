from django.contrib import admin
from django.forms.models import model_to_dict
from django.contrib.admin.models import LogEntry
from .models import human_type, human, demand, demand_status, priority

import logging

logger = logging.getLogger('ajms')

@admin.register(priority)
class priorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_code', 'description')
    list_editable = ['color_code']

    def log_change(self, request, object, message):
        new_message = []
        for item in message:
            obj = item
            obj["changed"]["values"] = object.to_dict()
            new_message.append(obj)
        super(priorityAdmin, self).log_change(request, object, new_message)

    def log_addition(self, request, object, message):
        new_message = []
        value = {}
        value["added"] = {}
        value["added"]["values"] = object.to_dict()
        new_message.append(value)
        super(priorityAdmin, self).log_addition(request, object, new_message)


@admin.register(human_type)
class human_typeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'color_code', 'description')
    list_editable = ['color_code']

    def log_change(self, request, object, message):
        new_message = []
        for item in message:
            obj = item
            obj["changed"]["values"] = object.to_dict()
            new_message.append(obj)
        super(human_typeAdmin, self).log_change(request, object, new_message)

    def log_addition(self, request, object, message):
        new_message = []
        value = {}
        value["added"] = {}
        value["added"]["values"] = object.to_dict()
        new_message.append(value)
        super(human_typeAdmin, self).log_addition(request, object, new_message)

@admin.register(human)
class humanAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'colored_human_type', 'shortname', 'phone', 'email')
    # list_display = ('name', 'get_human_type_display', 'shortname', 'phone', 'email')
    list_per_page = 20
    list_filter = ('company', 'deparment')
    search_fields = ('name', 'humantype', 'company', 'deparment', 'title', 'phone', 'email')
    fieldsets = (
        ['个人信息', {
            'fields': ('name', 'humantype')
        }], 
        ['公司信息', {
            'fields': ('company', 'deparment', 'title')
        }], 
        ['联系信息', {
            'fields': ('phone', 'email')
        }]
    )

    def log_change(self, request, object, message):
        new_message = []
        for item in message:
            obj = item
            obj["changed"]["values"] = object.to_dict()
            new_message.append(obj)
        super(humanAdmin, self).log_change(request, object, new_message)

    def log_addition(self, request, object, message):
        new_message = []
        value = {}
        value["added"] = {}
        value["added"]["values"] = object.to_dict()
        new_message.append(value)
        print(new_message)
        super(humanAdmin, self).log_addition(request, object, new_message)

@admin.register(demand)
class demandAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('need_auto', 'name', 'colored_priority', 'colored_status', 'publish_date', 'publisher', 'publisher_department', 'firster', 
    'ask_end_date', 'plan_begin_date', 'plan_end_date', 'processor', 'percent')
    list_per_page = 20
    readonly_fields = ('publish_date', )
    # fieldsets = ('name', 'publisher', 'publish_date', 'priority', 'processor', 'percent')
    fieldsets = (
        [
            '基本信息', {
                'fields': (('name', 'need_auto'), ('priority', 'status'))
            }
        ], 
        [
            '需求方信息', {
                'fields': (('publisher', 'firster'), 'ask_end_date')
            }
        ], 
        [
            '承接方信息', {
                'fields': ('processor', ('plan_begin_date', 'plan_end_date'))
            }
        ], 
        [
            '详细信息', {
                'fields': ('description',)
            }
        ], 
    )
    list_filter = ('priority', 'publisher', 'processor')
    search_fields = ('name', 'publisher', 'processor')
    list_editable = ['percent', ]
    date_hierarchy = 'publish_date'

    def log_change(self, request, object, message):
        new_message = []
        for item in message:
            obj = item
            obj["changed"]["values"] = object.to_dict()
            new_message.append(obj)
        super(demandAdmin, self).log_change(request, object, new_message)

    def log_addition(self, request, object, message):
        new_message = []
        value = {}
        value["added"] = {}
        value["added"]["values"] = object.to_dict()
        new_message.append(value)
        super(demandAdmin, self).log_addition(request, object, new_message)

@admin.register(demand_status)
class demand_statusAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'color_code', 'description')
    list_editable = ['color_code']

    def log_change(self, request, object, message):
        new_message = []
        for item in message:
            obj = item
            obj["changed"]["values"] = object.to_dict()
            new_message.append(obj)
        super(demand_statusAdmin, self).log_change(request, object, new_message)

    def log_addition(self, request, object, message):
        new_message = []
        value = {}
        value["added"] = {}
        value["added"]["values"] = object.to_dict()
        new_message.append(value)
        super(demand_statusAdmin, self).log_addition(request, object, new_message)

admin.site.register(LogEntry)

admin.site.site_header = 'Asiainfo Jobs Managment System'
admin.site.site_title = 'AJMS'
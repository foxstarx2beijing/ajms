import logging
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html

from comm.models import color_info
from .enums import enum_human_type, enum_human_type_info

logger = logging.getLogger('ajms')

class human_type(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '类型名称')
    color_code = models.ForeignKey(color_info, blank = False, on_delete = models.SET('000000'), verbose_name = '颜色代码')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '参与人类型'
        verbose_name_plural = '参与人类型'

class human(models.Model):
    company = models.CharField(max_length = 100, blank = True, verbose_name = '公司')
    deparment = models.CharField(max_length = 100, blank = True, verbose_name = '部门')
    name = models.CharField(max_length = 100, blank = False, verbose_name = '姓名')
    title = models.CharField(max_length = 100, blank = True, verbose_name = '职务')
    humantype = models.ForeignKey(human_type, blank = False, on_delete = models.PROTECT, verbose_name = '类型')
    phone = models.CharField(max_length = 20, blank = True, verbose_name = '电话号码')
    email = models.EmailField(blank = True, verbose_name = 'Email')

    def __str__(self):
        return self.name

    def colored_human_type(self):
        return format_html(
            '<span style="color: #{};font-weight:bold">{}</span>',
            self.humantype.color_code.color_code,
            self.humantype.name,
        )
    colored_human_type.short_description = '类型'

    def shortname(self):
        return "%s-%s-%s" % (self.company, self.deparment, self.title)

    shortname.short_description = '归属信息'

    class Meta:
        verbose_name = '参与人'
        verbose_name_plural = '参与人'
    
class demand_status(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '状态名称')
    color_code = models.ForeignKey(color_info, on_delete = models.SET('000000'), blank = False, verbose_name = '颜色配置')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '需求状态'
        verbose_name_plural = '需求状态'


class demand(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '需求名称')
    publisher = models.ForeignKey(human, on_delete = models.CASCADE, related_name = '需求人', verbose_name = '需求人')
    publish_date = models.DateField(auto_now_add = True, verbose_name = '需求日期')
    priority = models.IntegerField(default = '4', verbose_name = '优先级')
    processor = models.ForeignKey(human, on_delete = models.CASCADE, related_name = '承接人', verbose_name = '承接人')
    percent = models.IntegerField(blank = True, verbose_name = '进度')
    # status = models.CharField(max_length = 10, blank = False, choices = enum_demand_status, verbose_name = '状态')
    status = models.ForeignKey(demand_status, on_delete = models.PROTECT, related_name = '需求', verbose_name = '状态')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    def colored_status(self):
        return format_html(
            '<span style="color: #{};font-weight:bold">{}</span>',
            self.status.color_code.color_code,
            self.status.name,
        )
    colored_status.short_description = '状态'

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = '需求'
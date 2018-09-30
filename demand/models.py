import logging
import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils import timezone

from comm.models import color_info
from .enums import enum_human_type, enum_human_type_info

logger = logging.getLogger('ajms')

class priority(models.Model):
    name = models.CharField(max_length = 100, blank = True, verbose_name = '优先级名称')
    color_code = models.ForeignKey(color_info, blank = True, on_delete = models.PROTECT, verbose_name = '颜色代码')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    def to_dict(self):
        result = {}
        result["name"] = self.name
        result["color_code"] = self.color_code.pk
        result["description"] = self.description
        return result

    class Meta:
        verbose_name = '优先级'
        verbose_name_plural = '优先级'

class human_type(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '类型名称')
    color_code = models.ForeignKey(color_info, blank = False, on_delete = models.PROTECT, verbose_name = '颜色代码')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    def to_dict(self):
        result = {}
        result["name"] = self.name
        result["color_code"] = self.color_code.pk
        result["description"] = self.description
        return result

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

    def to_dict(self):
        result = {}
        result["company"] = self.company
        result["deparment"] = self.deparment
        result["name"] = self.name
        result["title"] = self.title
        result["humantype"] = self.humantype.pk
        result["phone"] = self.phone
        result["email"] = str(self.email)
        return result

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

    def to_dict(self):
        result = {}
        result["name"] = self.name
        result["color_code"] = self.color_code.pk
        result["description"] = self.description
        return result

    class Meta:
        verbose_name = '需求状态'
        verbose_name_plural = '需求状态'


class demand(models.Model):
    need_auto = models.BooleanField(verbose_name = '固化', default = True)
    name = models.CharField(max_length = 100, blank = False, verbose_name = '需求名称')
    firster = models.ForeignKey(human, blank = True, on_delete = models.PROTECT, related_name = '甲方对接人', verbose_name = '甲方对接人')
    publisher = models.ForeignKey(human, blank = True, on_delete = models.PROTECT, related_name = '需求人', verbose_name = '需求人')
    publish_date = models.DateField(auto_now_add = True, verbose_name = '需求日期')
    ask_end_date = models.DateField(verbose_name = '要求完成日期', blank = True, default = timezone.now)
    plan_begin_date = models.DateField(verbose_name = '计划开发日期', blank = True, default = timezone.now)
    plan_end_date = models.DateField(verbose_name = '计划完成日期', blank = True, default = timezone.now)
    priority = models.ForeignKey(priority, on_delete = models.PROTECT, verbose_name = '优先级')
    processor = models.ForeignKey(human, blank = True, on_delete = models.PROTECT, related_name = '承接人', verbose_name = '承接人')
    percent = models.IntegerField(blank = True, verbose_name = '进度', default = 0)
    # status = models.CharField(max_length = 10, blank = False, choices = enum_demand_status, verbose_name = '状态')
    status = models.ForeignKey(demand_status, on_delete = models.PROTECT, related_name = '需求', verbose_name = '状态')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    def to_dict(self):
        result = {}
        result["need_auto"] = self.need_auto
        result["name"] = self.name
        result["firster"] = self.firster.pk
        result["publisher"] = self.publisher.pk
        result["publish_date"] = str(self.publish_date)
        result["ask_end_date"] = str(self.ask_end_date)
        result["plan_begin_date"] = str(self.plan_begin_date)
        result["plan_end_date"] = str(self.plan_end_date)
        result["priority"] = self.priority.pk
        result["processor"] = self.processor.pk
        result["percent"] = self.percent
        result["status"] = self.status.pk
        result["description"] = self.description
        return result

    def publisher_department(self):
        return self.publisher.deparment
    publisher_department.short_description = '需求部门'

    def colored_status(self):
        return format_html(
            '<span style="color: #{};font-weight:bold">{}</span>',
            self.status.color_code.color_code,
            self.status.name,
        )
    colored_status.short_description = '状态'

    def colored_name(self):
        return format_html(
            '<span style="color: #{};font-weight:bold">{}</span>',
            self.priority.color_code.color_code,
            '【%s】%s' % (self.priority.name, self.name),
        )
    colored_name.short_description = '需求名称'

    def colored_priority(self):
        return format_html(
            '<span style="color: #{};font-weight:bold">{}</span>', 
            self.priority.color_code.color_code,
            self.priority.name,
        )
    colored_priority.short_description = '优先级'

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = '需求'

class demand_step(models.Model):
    title = models.CharField(max_length = 200, blank = True, verbose_name = '标题')
    demand_obj = models.ForeignKey(demand, blank = False, on_delete = models.PROTECT, related_name = '步骤', verbose_name = '需求')
    insert_date = models.DateField(auto_now_add = True, verbose_name = '添加日期')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    class Meta:
        verbose_name = '步骤'
        verbose_name_plural = '步骤'
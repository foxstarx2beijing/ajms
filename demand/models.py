from django.db import models
from .enums import enum_human_type

class human(models.Model):
    company = models.CharField(max_length = 100, blank = True, verbose_name = '公司')
    deparment = models.CharField(max_length = 100, blank = True, verbose_name = '部门')
    name = models.CharField(max_length = 100, blank = False, verbose_name = '姓名')
    title = models.CharField(max_length = 100, blank = True, verbose_name = '职务')
    human_type = models.CharField(max_length = 100, blank = True, choices = enum_human_type, verbose_name = '身份类型', default = enum_human_type[0][1])
    phone = models.CharField(max_length = 20, blank = True, verbose_name = '电话号码')
    email = models.EmailField(blank = True, verbose_name = 'Email')

    def __str__(self):
        return self.name

    def shortname(self):
        return "%s-%s-%s" % (self.company, self.deparment, self.title)

    shortname.short_description = '归属信息'

    class Meta:
        verbose_name = '参与人'
        verbose_name_plural = '参与人'

# class publisher(human):
#     human_type = models.CharField(max_length = 100, blank = True, choices = enum_human_type)

#     class __init__():
#         human_type = enum_human_type[1][1]

#     class Meta:
#         verbose_name = '需求人员'
#         verbose_name_plural = '需求人员'

# class processor(human):
#     human_type = models.CharField(max_length = 100, blank = True, choices = enum_human_type)

#     class __init__():
#         human_type = enum_human_type[2][1]

#     class Meta:
#         verbose_name = '承接人'
#         verbose_name_plural = '承接人'

class demand(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '需求名称')
    publisher = models.ForeignKey(human, on_delete = models.CASCADE, related_name = '需求人')
    publish_date = models.DateField(auto_now_add = True, verbose_name = '需求日期')
    priority = models.IntegerField(default = '4', verbose_name = '优先级')
    processor = models.ForeignKey(human, on_delete = models.CASCADE, related_name = '承接人')
    percent = models.IntegerField(blank = True, verbose_name = '进度')

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = '需求'
from django.db import models

class human(models.Model):
    company = models.CharField(max_length = 100, blank = True, verbose_name = '公司')
    deparment = models.CharField(max_length = 100, blank = True, verbose_name = '部门')
    name = models.CharField(max_length = 100, blank = False, verbose_name = '姓名')
    title = models.CharField(max_length = 100, blank = True, verbose_name = '职务')
    human_type = models.CharField(max_length = 100, blank = True, choices = (('0', '未分类'), ('1', '需求方'), ('2', '承接方')), default = 0, verbose_name = '角色')
    phone = models.CharField(max_length = 20, blank = True, verbose_name = '电话号码')
    email = models.EmailField(blank = True, verbose_name = 'Email')

    def __str__(self):
        return self.name

    def shortname(self):
        return "%s-%s-%s" % (self.company, self.deparment, self.title)

    shortname.short_description = '归属信息'

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员'

class demand(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '需求名称')
    publisher = human()
    publish_date = models.DateField(auto_now_add = True, verbose_name = '需求日期')
    priority = models.IntegerField(default = '4', verbose_name = '优先级')
    processor = human()
    percent = models.IntegerField(blank = True, verbose_name = '进度')

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = '需求'
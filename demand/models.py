from django.db import models

class human(models.Model):
    company = models.CharField(max_length = 100, blank = True)
    deparment = models.CharField(max_length = 100, blank = True)
    name = models.CharField(max_length = 100, blank = False)
    title = models.CharField(max_length = 100, blank = True)
    human_type = models.CharField(max_length = 100, blank = True, choices = (('0', '未分类'), ('1', '需求方'), ('2', '承接方')), default = 0)
    phone = models.CharField(max_length = 20, blank = True)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员'
        verbose_name_plural = '人员'

class demand(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    publisher = human()
    publish_date = models.DateField(auto_now_add = True)
    priority = models.IntegerField(default = '4')
    processor = human()
    percent = models.IntegerField(blank = True)

    class Meta:
        verbose_name = '需求'
        verbose_name_plural = '需求'
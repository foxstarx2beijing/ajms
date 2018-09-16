from django.db import models

class color_info(models.Model):
    name = models.CharField(max_length = 100, blank = False, verbose_name = '颜色名称')
    color_code = models.CharField(max_length = 10, blank = True, verbose_name = '颜色代码')
    description = models.TextField(max_length = 2000, blank = True, verbose_name = '描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '颜色代码'
        verbose_name_plural = '颜色代码'
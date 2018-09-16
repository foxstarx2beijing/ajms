# Generated by Django 2.1 on 2018-09-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0005_auto_20180916_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand_status',
            name='color_code',
            field=models.ForeignKey(on_delete=models.SET('000000'), to='comm.color_info', verbose_name='颜色配置'),
        ),
        migrations.AlterField(
            model_name='human_type',
            name='color_code',
            field=models.ForeignKey(on_delete=models.SET('000000'), to='comm.color_info', verbose_name='颜色代码'),
        ),
    ]

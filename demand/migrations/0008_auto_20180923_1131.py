# Generated by Django 2.1 on 2018-09-23 03:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0007_auto_20180917_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='ask_end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 9, 23, 3, 30, 42, 992909, tzinfo=utc), verbose_name='要求完成日期'),
        ),
        migrations.AddField(
            model_name='demand',
            name='firster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='甲方对接人', to='demand.human', verbose_name='甲方对接人'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='demand',
            name='need_auto',
            field=models.BooleanField(default=True, verbose_name='是否需要固化'),
        ),
        migrations.AddField(
            model_name='demand',
            name='plan_begin_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 9, 23, 3, 30, 42, 992909, tzinfo=utc), verbose_name='计划开发日期'),
        ),
        migrations.AddField(
            model_name='demand',
            name='plan_end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 9, 23, 3, 30, 42, 992909, tzinfo=utc), verbose_name='计划完成日期'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='processor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='承接人', to='demand.human', verbose_name='承接人'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='需求人', to='demand.human', verbose_name='需求人'),
        ),
    ]
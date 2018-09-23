# Generated by Django 2.1 on 2018-09-23 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0001_initial'),
        ('demand', '0009_auto_20180923_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='优先级名称')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='描述')),
                ('color_code', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='comm.color_info', verbose_name='颜色代码')),
            ],
            options={
                'verbose_name': '优先级',
                'verbose_name_plural': '优先级',
            },
        ),
        migrations.AlterField(
            model_name='demand',
            name='need_auto',
            field=models.BooleanField(default=True, verbose_name='需要固化'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='percent',
            field=models.IntegerField(blank=True, default=0, verbose_name='进度'),
        ),
        migrations.AlterField(
            model_name='human_type',
            name='color_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comm.color_info', verbose_name='颜色代码'),
        ),
    ]

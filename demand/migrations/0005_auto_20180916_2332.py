# Generated by Django 2.1 on 2018-09-16 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0004_auto_20180916_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='human_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='类型名称')),
                ('color_code', models.CharField(blank=True, max_length=10, verbose_name='颜色代码')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='描述')),
            ],
            options={
                'verbose_name': '参与人类型',
                'verbose_name_plural': '参与人类型',
            },
        ),
        migrations.AlterField(
            model_name='demand_status',
            name='color_code',
            field=models.ForeignKey(blank=True, on_delete=models.SET('000000'), to='comm.color_info', verbose_name='颜色配置'),
        ),
        migrations.AlterField(
            model_name='human',
            name='human_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demand.human_type', verbose_name='类型'),
        ),
    ]

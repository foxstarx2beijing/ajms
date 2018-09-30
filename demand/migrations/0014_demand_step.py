# Generated by Django 2.1 on 2018-09-30 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0013_auto_20180924_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='demand_step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insert_date', models.DateField(auto_now_add=True, verbose_name='完成日期')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='描述')),
                ('demand_obj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='步骤', to='demand.demand', verbose_name='需求')),
            ],
            options={
                'verbose_name': '步骤',
                'verbose_name_plural': '步骤',
            },
        ),
    ]
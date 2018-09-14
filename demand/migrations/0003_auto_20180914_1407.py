# Generated by Django 2.1 on 2018-09-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0002_demand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': '需求', 'verbose_name_plural': '需求'},
        ),
        migrations.AlterModelOptions(
            name='human',
            options={'verbose_name': '人员', 'verbose_name_plural': '人员'},
        ),
        migrations.AddField(
            model_name='human',
            name='human_type',
            field=models.CharField(blank=True, choices=[('需求方', '需求'), ('承接方', '惩戒')], max_length=100),
        ),
        migrations.AddField(
            model_name='human',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

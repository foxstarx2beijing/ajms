# Generated by Django 2.1 on 2018-09-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='description',
            field=models.TextField(blank=True, max_length=2000, verbose_name='描述'),
        ),
    ]

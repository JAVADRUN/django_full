# Generated by Django 3.2.16 on 2022-12-28 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prj', '0002_auto_20221217_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipaddress',
            options={'verbose_name_plural': 'آی پی کاربران'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]

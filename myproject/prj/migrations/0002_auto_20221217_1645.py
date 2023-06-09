# Generated by Django 3.2.16 on 2022-12-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی پی')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='prj.IPAddress', verbose_name='بازدیدها'),
        ),
    ]

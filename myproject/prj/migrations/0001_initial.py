# Generated by Django 3.2.6 on 2022-11-19 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='javad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان مقالات')),
                ('slug', models.SlugField(max_length=100, verbose_name='آدرس مقالات')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=300, verbose_name='آدرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='prj.category', verbose_name='زیر دسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان مقالات')),
                ('slug', models.SlugField(max_length=100, verbose_name='آدرس مقالات')),
                ('descriptions', models.TextField(verbose_name='محتوا')),
                ('images', models.ImageField(upload_to=True, verbose_name='تصویر مقالات')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('F', 'پیشنویس'), ('T', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=10, verbose_name='وضعیت')),
                ('is_special', models.BooleanField(default=False, verbose_name='مقاله ویژه')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='articles', to='prj.Category', verbose_name='دسته بندی ')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]

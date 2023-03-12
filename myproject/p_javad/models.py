from django.utils import timezone
from django.db import models

# Create your models here.

class Mobile_Article(models.Model):
    STATUS = (
        ('LG' , 'lg'),
        ('Samsung' , 'samsung'),
        ('Xiaomi' , 'xiaomi'),
        ('HP' , 'hp'),
        ('TSCO' , 'tsco'),
    )

    title = models.CharField(max_length=150 , verbose_name='نام')
    slug = models.SlugField(max_length=200)
    images = models.ImageField(upload_to=True , verbose_name='عکس')
    descriptions = models.TextField(verbose_name='توضیحات')
    publish = models.DateTimeField(default=timezone.now , verbose_name='زمان انتشار')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(verbose_name='قیمت')
    status = models.CharField(max_length=60 , verbose_name='برند' , choices=STATUS)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه جواد"
    
       
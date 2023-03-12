from re import T
from django.urls import reverse
from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from account.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

#https://docs.djangoproject.com/en/4.1/topics/db/models/

# my Article_Maneger
class Article_Maneger(models.Manager):
    def status(self):
        return self.filter(status = "T")
# my Article_Maneger    
class category_Maneger(models.Manager):
    def active(self):
        return self.filter(status =True)    
# IPAddress 
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی')

    class Meta:
        verbose_name_plural = 'آی پی کاربران'

# Category
class Category(models.Model):
    parent =models.ForeignKey('self',  default=None , blank=True, null=True , on_delete=models.SET_NULL , related_name='children' , verbose_name='زیر دسته')
    name = models.CharField(max_length= 200 , verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length= 300 , verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True , verbose_name='آیا نمایش داده شود')
    position = models.IntegerField(verbose_name= 'پوزیشن')
                    
    # stering name Category
    def __str__(self):
        return self.name 
    
    # Meta objects Category
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id','position']

    objects = category_Maneger() 
    
    
# class Article
class Article(models.Model):
    STATUS = (
      ('F' , 'پیشنویس'), # draft
      ('T' , 'منتشر شده'), # publish
      ('i' , 'در حال بررسی'), # investigaion
      ('b' , 'برگشت داده شده'), #back

    )
    author = models.ForeignKey(User , null=True , on_delete=models.SET_NULL , related_name="articles" , verbose_name= "نویسنده")
    name = models.CharField(max_length=200 , verbose_name='عنوان مقالات')
    slug = models.SlugField(max_length=100 , verbose_name = 'آدرس مقالات')
    descriptions = models.TextField(verbose_name='محتوا')
    images = models.ImageField(upload_to=True , verbose_name ='تصویر مقالات') 
    publish = models.DateTimeField(default=timezone.now ,verbose_name ='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS , verbose_name ='وضعیت')
    is_special = models.BooleanField(default=False , verbose_name='مقاله ویژه')
    category = models.ManyToManyField(Category ,verbose_name='دسته بندی ', related_name='articles')
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress , through="ArticleHit", blank=True , related_name="hits" , verbose_name='بازدیدها')
    
    # stering name Article
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("account:home")
    # Meta objects Article
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    # detatime jpublish extensions Article
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    # Maneger Article_Maneger
    
    def images_tag(self):
        return format_html("<img width='100' height='100' style='border-radius: 5px;' src='{}'>".format(self.images.url))            
    images_tag.short_description = " عکس"
    objects = Article_Maneger()
    
    def category_to_str(self):
        return " , ".join([category.name for category in self.category.active()])
    category_to_str.short_description = 'دسته بندی ها'

# We can make all our status in the same way by using these
#   def make_published(modeladmin, request, queryset):
#     queryset.update(status='T')

class ArticleHit(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


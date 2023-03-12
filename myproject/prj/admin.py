from django.contrib import admin
from .models import Article , Category , IPAddress
from django.contrib import messages
from django.utils.translation import ngettext
#https://docs.djangoproject.com/en/4.1/ref/contrib/admin/

# Register your models here.

# @admin.action(description='Mark selected stories as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='T')

# # Globally disable delete selected
# admin.site.disable_action('delete_selected')

admin.site.site_header = "وبلاگ جنگویی من"

def make_published(modeladmin, request, queryset):
        updated = queryset.update(status='T')
        modeladmin.message_user(request, ngettext(
            '%d مقاله منتشر شد.',
            '%d مقاله منتشر شد.',
            updated,
        ) % updated, messages.SUCCESS)
make_published.short_description ="مقالات منتشر شده"

def make_draft(modeladmin, request, queryset):
        updated = queryset.update(status='F')
        modeladmin.message_user(request, ngettext(
            '%d مقاله پیشنویس شد.',
            '%d مقاله پیشنویس شد.',
            updated,
        ) % updated, messages.SUCCESS)
make_draft.short_description ="مقالات پیشنویس شده"

# class admin Article models
class Article_admin(admin.ModelAdmin):
    list_display =('name' ,'images_tag', 'status','author' ,'jpublish' , 'category_to_str' , 'is_special')
    search_fields = ('name' , 'slug' ,)
    list_filter = ('slug',)
    actions = [make_published , make_draft]
    # prepopulated_fields = {'slug':('name' ,)}
    # ordering = ['-status' , '-publish']
    # exclude = ['name' ,]
    

# register admin Article
admin.site.register(Article , Article_admin)

def make_published(modeladmin, request, queryset):
        updated = queryset.update(status='True')
        modeladmin.message_user(request, ngettext(
            '%d مقاله منتشر شد.',
            '%d مقاله منتشر شد.',
            updated,
        ) % updated, messages.SUCCESS)
make_published.short_description ="مقالات منتشر شده"

def make_draft(modeladmin, request, queryset):
        updated = queryset.update(status='False')
        modeladmin.message_user(request, ngettext(
            '%d مقاله پیشنویس شد.',
            '%d مقاله پیشنویس شد.',
            updated,
        ) % updated, messages.SUCCESS)
make_draft.short_description ="مقالات پیشنویس شده"

    
# class admin Category models
class Category_admin(admin.ModelAdmin):
    list_display =('position','name' , 'slug','parent' , 'status' ,)
    search_fields = ('name' , 'slug' ,)
    list_filter = (['status'])
    actions = [make_published , make_draft]
    
# register admin Category
admin.site.register(Category , Category_admin)



# register admin IPAddress
admin.site.register(IPAddress)












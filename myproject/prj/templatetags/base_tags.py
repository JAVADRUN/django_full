from django import template
from ..models import Category , Article
from django.db.models import Count , Q 
from datetime import datetime , timedelta
#https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/

register = template.Library()

# tags Category 1
 # def test(deta = 'وبلاگ جگویی'):
 #     return deta
 
# tags Category 2
@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.simple_tag
def login_title():
    return "Login"


# tags Category 3
@register.inclusion_tag("prj/partials/category_navbar.html")
def category_navbar():
    return{
        'category':Category.objects.filter(status = True)
    }
    
# @register.inclusion_tag("registration/partials/link.html")
# def link(request , link_name , content , clases):
#     return{
#         "request":request,
#         "link_name":link_name,
#         "link":"account:{}".format(link_name),
#         "content":content,
#         "clases":clases,

#     }


@register.inclusion_tag("prj/partials/sidebar.html")

def popular_article():
    last_month = datetime.today() - timedelta(days=30)
    return{
        'articles': Article.objects.status().annotate(
        count=Count('hits' , filter=Q(articlehit__created__gt=last_month))
        ).order_by('-count' , '-publish')[ :5],
        'title' : "مقالات پر بازدید ماه" 
    }

@register.inclusion_tag("prj/partials/sidebar.html")

def hot_article():
    last_month = datetime.today() - timedelta(days=30)
    return{
        'articles': Article.objects.status().annotate(
        count=Count('comments' , filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id=6))
        ).order_by('-count' , '-publish')[ :5],
        'title' : "مقالات داغ" 
    }



    
	
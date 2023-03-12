from django.urls import path
from .views import (
    ArticleListview,
    ArticleDetail,
    categoryList,
    ArticlePreview,
    authorList

)
# https://docs.djangoproject.com/en/4.1/topics/http/urls/ 

app_name ='prj'
urlpatterns = [
    path('home/' , ArticleListview.as_view() , name='home'),
    path('page/<int:page>' , ArticleListview.as_view() , name='home'),
    path('detail/<slug:slug>' , ArticleDetail.as_view() , name='detail'),
    path('preview/<int:pk>' , ArticlePreview.as_view() , name='preview'),
    path('category/<slug:slug>' , categoryList.as_view() , name='category'),
    path('category/<slug:slug>/page/<int:page>' , categoryList.as_view() , name='category'),
    path('author/<slug:username>' , authorList.as_view() , name='author'),
    path('author/<slug:username>/page/<int:page>' , authorList.as_view() , name='author'),

]

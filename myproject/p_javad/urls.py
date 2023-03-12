from django.urls import path
from .views import mobile , id_mobile
app_name ='p_javad'
urlpatterns = [
    path('mobile/' , mobile , name='mobile.com'),   
    path('<slug:slug>' , id_mobile , name='id_mobile'),

]
 
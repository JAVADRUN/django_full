from django.apps import AppConfig
#https://docs.djangoproject.com/en/4.1/ref/applications/

class PrjConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prj'
    verbose_name = 'وبلاگ'

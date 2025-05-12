from django.urls import path
from . import views
name_app = 'core'

urlpatterns = [
    path('', views.create, name="home"),
    path('', views.update, name="home"),
    path('', views.list, name="home"),
    path('', views.delete, name="home"),
]

from django.urls import path

from . import views

app_name = 'r_umetea'
urlpatterns = [
    path('/main', views.main, name='main'),
    path('/front', views.front, name='front'),
]
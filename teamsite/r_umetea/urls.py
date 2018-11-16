from django.urls import path

from . import views

app_name = 'r_umetea'
urlpatterns = [
    path('/main', views.main, name='main'),
    path('/response_test', views.response_test, name='response_test'),
    path('/front', views.front, name='front'),
    path('/about', views.about, name='about'),
    path('/error', views.error, name='error'),
]
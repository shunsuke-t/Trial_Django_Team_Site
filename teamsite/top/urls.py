from django.urls import path,include
from . import views

app_name = 'top'
urlpatterns = [
    path('', views.index, name='index'),
]

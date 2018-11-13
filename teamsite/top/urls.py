from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'r_umetea/',include('r_umetea.urls')),
]
from django.urls import path

from . import views

app_name = "indix"

urlpatterns = [
    path('', views.indix, name='index'),
]
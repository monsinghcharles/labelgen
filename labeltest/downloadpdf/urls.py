from django.urls import path

from . import views

app_name = "download"

urlpatterns = [
    path('', views.download, name='downloadpdf'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('filesave/', views.fileSave),
    path('api/filesave/put', views.filePut),
]
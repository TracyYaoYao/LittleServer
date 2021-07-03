from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.home),
    path('tinyurl/', views.tinyurl),
    path('api/tinyurl/encode', views.tinyurlEncode),
    path('api/tinyurl/decode', views.tinyurlDecode),
    path('r/<str:turl>',views.tinyurlRedirect),

]

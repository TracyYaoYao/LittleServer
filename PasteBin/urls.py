from django.urls import path
from . import views



urlpatterns = [
    path('pastebin/', views.pastebin),
    path('api/pastebin/submit', views.pasteSubmit),
    path('p/<str:turl>',views.syntaxShow),

]

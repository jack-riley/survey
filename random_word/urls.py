from django.urls import path
from . import views	

urlpatterns = [
    path ('', views.random),
    path('/', views.random),
    path ('/reset', views.reset),
    path ('/reset/', views.reset),

]
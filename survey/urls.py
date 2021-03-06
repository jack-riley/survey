from django.urls import path
from . import views	

urlpatterns = [
    path ('', views.form),
    path ('result', views.results),
    path ('display', views.display)
]

from django.urls import path
from panel import views

urlpatterns = [
    path('', views.home, name="home")
]
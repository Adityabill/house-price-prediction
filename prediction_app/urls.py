from prediction_app import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name = 'home page'),
]
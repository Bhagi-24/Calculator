from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('result/', views.result_view, name='result'),
]

from django.urls import path
from . import views 

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('data-throw/', views.data_throw, name='throw'),
    path('data-catch/', views.data_catch, name='catch'),
]
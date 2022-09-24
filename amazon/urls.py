from django.urls import path
from django.contrib import admin
from amazon.views import carIndex,CarDetails,CreateCarView,EditCarView,DeleteCarView
urlpatterns = [
    path('index',carIndex),
    path('<int:pk>',CarDetails.as_view(),name='amazon.show'),
    path('create',CreateCarView.as_view()),
    path('edit/<int:pk>', EditCarView.as_view(), name='amazon.edit'),
    path('delete/<int:pk>', DeleteCarView.as_view(), name='amazon.delete'),

]
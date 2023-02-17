from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('create/',views.create,name='create'),
   path("read/",views.read_data,name='json'),
   path("update/<int:id>/",views.update_data,name='update'),
]
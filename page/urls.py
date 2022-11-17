from django.contrib import admin
from django.urls import path
from .views import index, rekruto

urlpatterns = [
    path('', index.as_view()),
    path('url_name/', rekruto.as_view(), name='task')
]
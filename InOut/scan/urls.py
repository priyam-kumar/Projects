from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('saveRecord/', views.saveRecord),
]

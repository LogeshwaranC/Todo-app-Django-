from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path ('update_task/<str:pk>/', views.update_task , name = 'update_task'),
    path ('detetetask/<str:pk>/', views.deletetask, name ='deletetask'),
]
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.main_view, name='home'),
    path('update_task/<str:slug>/', views.Task_update_View, name='update_task'),
    path('get/ajax/del_task', views.Delete_Task, name='del_task')
]

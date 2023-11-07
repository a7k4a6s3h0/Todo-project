from django.urls import path
from . import views

# <..........................FUNCTION BASED VIEWS URLS..............................>

# urlpatterns = [
    
#     path('',views.main_view, name='home'),
#     path('update_task/<str:slug>/', views.Task_update_View, name='update_task'),
#     path('get/ajax/del_task', views.Delete_Task, name='del_task')
# ]



# <..........................CLASS BASED VIEWS URLS..............................>

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('update_task/<str:slug>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('get/ajax/del_task', views.DeleteTaskView.as_view(), name='del_task')
]
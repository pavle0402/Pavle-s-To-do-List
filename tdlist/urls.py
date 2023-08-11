from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home_page, name='login'),
    path('about/', views.about_page, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('tasks_list/', login_required(views.CreateTaskView.as_view()), name='tasks_list'),
    path('tasks_list/create_task/', login_required(views.CreateTaskView.as_view()), name='create_task'),
    path('tasks_list/<int:pk>/delete/', login_required(views.DeleteTaskView.as_view()), name='delete_task'),
    path('pin_task/<int:pk>/', views.PinTaskView, name="pin_task"),
    # path('tasks_list/<int:pk>/task_completed/', views.TaskCompletionUpdateView.as_view(), name="task_completed")
]
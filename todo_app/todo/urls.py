from django.http import request
from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView, home
from .import views
urlpatterns=[
    path('task-list/' ,TaskList.as_view(),name='task1'),
    path('task-create/' ,TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('task-detail/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('login/',views.login_fun,name='login'),
    path('register/',views.register_fun,name='Register'),
    path('',home,name='home'),
    path('mail/',views.mail)
]
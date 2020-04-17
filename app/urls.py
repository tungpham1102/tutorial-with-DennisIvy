from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list-view/', views.task_list_view, name='task-list-view'),
    path('task-create-view/', views.task_create_view, name='task-create-view'),
    path('task-detail-view/<int:pk>/', views.task_detail_view, name='task-detail-view'),
    path('task-update-view/<int:pk>/', views.task_update_view, name='task-update-view'),
    path('task-delete-view/<int:pk>/', views.task_delete_view, name='task-delete-view'),
]
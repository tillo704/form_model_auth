from django.urls import path
from .views import TasksListView,TasksCreateView,TasksUpdateView,TaskDeleteView

urlpatterns = [
    path('',TasksListView.as_view(), name='tasks-list'),
    path('create/', TasksCreateView.as_view(),name='task-create'),
    path('update/<int:pk>/', TasksUpdateView.as_view(),name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete')
]


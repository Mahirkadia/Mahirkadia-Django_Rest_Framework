from django.urls import path
from .views import *

urlpatterns =[
    path('api/projects',ProjectListCreate.as_view()),
    path('api/projects/<int:pk>/',ProjectDetails.as_view()),
    path('api/projects/<int:project_id>/tasks', TaskListCreate.as_view()),
    path('api/tasks/<int:pk>/',TaskDetail.as_view()),
    path('api/tasks/<int:task_id>/comments/',CommentListCreate.as_view()),
    path('api/comments/<int:pk>/', CommentDetail.as_view()),
]
from . import views
from django.urls import path


urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  path('task-list', views.taskList, name="task-list"),
  # path('task-list', views.taskList, name="task-list"),
]

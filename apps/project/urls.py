from django.urls import path

from . import views


app_name = 'project'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<slug:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('projects/', views.ProjectsView.as_view(), name='projects')
]

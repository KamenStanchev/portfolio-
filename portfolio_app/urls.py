from django.urls import path
from portfolio_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_list, name='projects-list'),
    path('projects/<str:pk>/', views.project_details, name='projects-details'),
]

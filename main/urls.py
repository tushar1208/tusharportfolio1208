from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('data_visualization/', views.data_visualization, name='data_visualization'),
    path('python/', views.python, name='python'),
    path('machine_learning/', views.machine_learning, name='machine_learning'),
    path('deep_learning/', views.deep_learning, name='deep_learning'),
]

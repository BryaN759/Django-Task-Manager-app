from django.urls import path
from . import views

urlpatterns = [

    #--------------------- Register route --------------------------#
    path('register/', views.register, name='register'),

    #--------------------- Login route --------------------------#
    path('login/', views.login, name='login'),

    #--------------------- Logout route --------------------------#
    path('logout/', views.logout, name='logout'),

    #--------------------- Home route --------------------------#
    path('', views.home, name='home'),

    #--------------------- Dashboard route --------------------------#
    path('dashboard/', views.dashboard, name='dashboard'),

    #--------------------- add Task route --------------------------#
    path('create/', views.createTask, name='create'),

    #--------------------- edit Task route --------------------------#
    path('edit/<str:pk>/', views.editTask, name='edit'),

    #--------------------- delete Task route --------------------------#
    path('delete/<str:pk>/', views.deleteTask, name='delete'),

]
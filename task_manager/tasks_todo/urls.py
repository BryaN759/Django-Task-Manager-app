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

    #--------------------- clear incomplete task route --------------------------#
    path('clear_incomplete_tasks/', views.clear_incomplete_tasks, name='clear_incomplete_tasks'),

    #--------------------- Clear complete task route --------------------------#
    path('clear_complete_tasks/', views.clear_complete_tasks, name='clear_complete_tasks'),

    #--------------------- Clear all task route --------------------------#
    path('clear_all_tasks/', views.clear_all_tasks, name='clear_all_tasks'),

    #--------------------- Profile route --------------------------#
    path('profile/', views.profile, name='profile'),

    #--------------------- Delete Profile route --------------------------#
    path('delete-profile/', views.deleteProfile, name='delete-profile'),


    #--------------------- add Task route --------------------------#
    path('create/', views.createTask, name='create'),

    #--------------------- edit Task route --------------------------#
    path('edit/<str:pk>/', views.editTask, name='edit'),

    #--------------------- delete Task route --------------------------#
    path('delete/<str:pk>/', views.deleteTask, name='delete'),

    #--------------------- search Task route --------------------------#
    path('search/', views.searchTask, name='search'),

]
from django.urls import path
from . import views
urlpatterns = [
     path("",views.home,name="home"),
     path("login/", views.login_view, name="login"),
     path("logout/", views.logout_view, name="logout"),
     path("register/", views.register_view, name="register"),
     path('allTask/', views.allTask, name='allTask'),
     path('addTask/', views.create_task, name='create_task'),
     path('edit/<int:id>/', views.update_task, name='update_task'),
     path('delete/<int:id>/', views.delete_task, name='delete_task'),
     path ('profile/', views.profile, name="profile"),
     path('update_status/<int:id>/', views.update_status, name='update_status'),
     path('assign_task/<int:id>/', views.assign_task, name='assign_task'),
     path('myTasks/', views.myTasks, name='myTasks'),
]
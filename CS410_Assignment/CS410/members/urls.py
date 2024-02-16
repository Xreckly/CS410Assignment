from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.register, name='student'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]
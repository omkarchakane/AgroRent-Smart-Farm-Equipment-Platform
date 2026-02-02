from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rent/<int:id>/', views.rent_equipment, name='rent'),
    path('history/', views.history, name='history'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

#! name is a unique label for a URL path.
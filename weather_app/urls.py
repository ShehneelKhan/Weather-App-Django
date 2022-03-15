from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [

    #path('', views.weather_data, name='weather_data'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='weather_app/login.html'), name='login'),  #(See settings.py bottom)
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),  #(See settings.py bottom)

    path('profile/', views.profile, name='profile'),

]

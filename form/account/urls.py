from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome.as_view(),name="welcome"),
    path('register', views.authentication.as_view(),name="register"),
    path('logout', views.logoutView.as_view(),name="logout"),
    path('login', views.LoginView.as_view(),name="login"),
]

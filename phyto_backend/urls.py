from django.urls import re_path, include, path

from . import views

app_name = "phyto_backend"
urlpatterns = [
    path('', views.index, name="home"),
    path('', include("django.contrib.auth.urls")),
    re_path("^login/?$", views.AuthenticateView.as_view(), name="login"),
    re_path("^signup/?$", views.RegistrationView.as_view(), name="register"),
]

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "files"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("upload/", views.upload_document, name="upload_document"),
    path("users/", views.user_list, name="user_list"),
    path("", views.document_list, name="document_list"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>/", views.delete_todo, name="delete_todo"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

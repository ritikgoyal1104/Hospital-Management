from django.urls import path

from . import views

urlpatterns = [
  path("",views.home_page , name="home_page"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("doctors",views.doctors , name="doctors"),
  path("profile",views.profile , name="profile"),
  path("appointment",views.appointment , name="appointment"),
]
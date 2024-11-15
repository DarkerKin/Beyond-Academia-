from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("room/",views.room, name="room"),
    path("safety/",views.safety,name="safety"),
    path("about/",views.about,name="about"),
    path("support/",views.support,name="support"),
    path("login/",views.login,name="Login"),
    path('room/<str:pk>/',views.room,name="room"),


]
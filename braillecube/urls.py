"""braillecube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import login_view, logout_view, signup_view, splash_view
from modules.views import home_view, clockrace_view, flashcards_view, freeplay_view, spaceman_view, level_select_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("login", login_view, name="login"),
    path("home", home_view, name="home"),
    path("clockrace/<str:id>", clockrace_view, name="clockrace"),
    path("flashcards/<str:id>", flashcards_view, name="flashcards"),
    path("freeplay", freeplay_view, name="freeplay"),
    path("spaceman/<str:id>", spaceman_view, name="spaceman"),
    path("level/<str:id>", level_select_view, name="level"),
    path("", splash_view, name="splash")
]

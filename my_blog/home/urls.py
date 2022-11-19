from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("register/", views.register, name="user-register"),
    path("register/update/", views.user_update, name="user-update"),
]


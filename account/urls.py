from django.urls import path, include, reverse
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    # path('edit/', views.edit, name='edit'),
]

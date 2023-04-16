from django.urls import path
from . import views

app_name = "MainApp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("result/<int:pk>", views.result, name="result"),
]

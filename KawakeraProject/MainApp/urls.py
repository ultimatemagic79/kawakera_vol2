from django.urls import path
from . import views

app_name = "MainApp"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("result", views.result, name="result"),
    path("", views.IndexView.as_view(), name="index"),
    path("result/", views.ResultView.as_view(), name="result"),
]

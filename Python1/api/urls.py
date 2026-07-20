from django.urls import path
from .views import ApiHomeView
from .views import (
    StudentListCreateAPI,
    StudentRetrieveUpdateDestroyAPI,
)

urlpatterns = [

    path(
        "students/",
        StudentListCreateAPI.as_view(),
        name="student_api",
    ),

    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPI.as_view(),
        name="student_api_detail",
    ),
    path("", ApiHomeView.as_view(), name="api_home"),
]
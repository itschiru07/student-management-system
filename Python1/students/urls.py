from django.urls import path
from .views import HomeView, StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView
urlpatterns = [

    path("", HomeView.as_view(), name="home"),

    path("students/", StudentListView.as_view(), name="student_list"),

    path("students/add/", StudentCreateView.as_view(), name="student_create"),

    path(
        "students/<int:student_id>/",
        StudentDetailView.as_view(),
        name="student_detail",
    ),

    path(
        "students/<int:student_id>/edit/",
        StudentUpdateView.as_view(),
        name="student_update",
    ),

    path(
        "students/<int:student_id>/delete/",
        StudentDeleteView.as_view(),
        name="student_delete",
    ),

]
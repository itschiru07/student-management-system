from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from students.models import Student
from .serializers import (
    StudentSerializer,
    StudentWriteSerializer,
)


class ApiHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Welcome to the Student Management API"
        })


class StudentListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StudentWriteSerializer
        return StudentSerializer


class StudentRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return StudentWriteSerializer
        return StudentSerializer
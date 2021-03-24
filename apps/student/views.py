from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from .models import Student
from .serializers import StudentSerializer


class StudentPagination(PageNumberPagination):
    page_size = 3


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination

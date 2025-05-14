from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.filter(passby='user1')
    serializer_class=StudentSerializer
    
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)
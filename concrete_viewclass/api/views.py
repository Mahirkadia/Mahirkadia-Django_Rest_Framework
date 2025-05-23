from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView, CreateAPIView ,RetrieveAPIView ,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
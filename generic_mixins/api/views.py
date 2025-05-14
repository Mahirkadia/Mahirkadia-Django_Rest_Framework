from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)    
    
    def post(self,request,*args,**kargs):
        return self.create(request, *args, **kargs)


class RUDStudentAPI(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    def get(self,request,*args,**kargs):
        return self.retrieve(request, *args, **kargs)

    def put(self,request,*args,**kargs):
        return self.update(request, *args, **kargs)

    def delete(self,request,*args,**kargs):
        return self.destroy(request,*args,**kargs)
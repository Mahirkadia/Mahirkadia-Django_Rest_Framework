from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class ProjectListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProjectDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        project = get_object_or_404(Project, pk=pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
    
    def put(self, request , pk):
        project = get_object_or_404(Project, pk=pk)
        serializers = ProjectSerializer(project, data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        project = get_object_or_404(Project,pk=pk)
        project.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
class TaskListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,project_id):
        tasks = Task.objects.filter(project_id=project_id)
        serializers = TaskSerializer(tasks, many = True)
        return Response(serializers.data)
    
    def post(self,request,project_id):
        data = request.data.copy()
        data['project'] = project_id
        serializers = TaskSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        task=get_object_or_404(Task, pk=pk)
        serializers = TaskSerializer(task)
        return Response(serializers.data)
    def put(self,request,pk):
        task = get_object_or_404(Task, pk=pk)
        serializers = TaskSerializer(task, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_404_NOT_FOUND)
    def delete(self, request , pk):
        task=get_object_or_404(Task,pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommnetListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,task_id):
        comment = Comment.objects.filter(task_id=task_id)
        serializers = CommentSerializer(comment, many=True)
        return Response(serializers.data)
    def post(self,request,task_id):
        data = request.data.copy()
        data['task'] = task_id
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TaskDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        task=get_object_or_404(Task, pk=pk)
        serializers = TaskSerializer(task)
        return Response(serializers.data)
    def put(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        serializers = TaskSerializer(task, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListCreate(APIView):
    permission_classes = [IsAuthenticated]
       
    def get(self,request,task_id):
        cmt = Comment.objects.filter(task_id=task_id)
        serializers = CommentSerializer(cmt, many=True)
        return Response(serializers.data)
    def post(self,request,task_id):
        data=request.data
        data['task'] = task_id
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class CommentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        cmt = get_object_or_404(Comment, pk=pk)
        serializers = CommentSerializer(cmt)
        return Response(serializers.data)
    def put(self,request,pk):
        cmt = get_object_or_404(Comment,pk=pk)
        serializers = CommentSerializer(cmt, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        cmt = get_object_or_404(Comment, pk=pk)
        cmt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
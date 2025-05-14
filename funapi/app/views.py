from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 

# @api_view(['GET'])
# def hello(request):
#     return Response({'msg':'hello world'})

@api_view(['GET', 'POST'])
def hello(request):
    if request.method =='GET':
        return Response({'msg':'This is a GET Msg'})
    if request.method =='POST':
        print(request.data)
        return Response({'msg':'This is a post method','data':request.data})

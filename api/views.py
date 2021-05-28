from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serialization import *

@api_view(['GET'])
def apiOverview(request):
    resp = {
        'desc' : 'Ini adalah API yang menjelaskan tentang startup yang ada di Indonesia dan juga informasi yang terkait'
    }
    return Response(resp)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def StartUpList(request):
    if request.method == 'GET':
        startup = StartUp.objects.all()
        serialization = StartUpSerialization(startup, many=True)
        return Response(serialization.data)
    elif request.method == 'POST':
        serialization = StartUpSerialization(data=request.data)
        if serialization.is_valid():
            serialization.save()
            return Response("Data berhasil dimasukan")
        else:
            return Response("Data gagal dimasukan")
    

@api_view(['GET', "PUT", 'DELETE'])
@permission_classes([IsAuthenticated])
def DetailStartup(request, pk):
    startup = StartUp.objects.get(id=pk)
    if request.method == 'GET':
        serializers = StartUpSerialization(startup, many = False)
        return Response(serializers.data)
    elif request.method == "PUT":
        serializers = StartUpSerialization(instance=startup, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("Data berhasil di update")
        else:
            return Response("Data gagal update", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        startup.delete()
        return Response("Data dihapus")
    

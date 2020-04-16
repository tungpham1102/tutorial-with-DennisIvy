from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
# Create your views here.


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list_view(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail_view(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return redirect('task-list-view')
    return Response(serializer.data)


@api_view(['POST'])
def task_update_view(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return redirect('task-list-view')
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete_view(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item was deleted")
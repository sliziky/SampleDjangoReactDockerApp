from .serializers import TaskSerializer
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from pymongo import MongoClient
from .models import Task

@api_view(['GET'])
def apiOverview(req):
  client = MongoClient('localhost', 27017)
  # First define the database name
  dbname = client['tasks']

  # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
  collection_name = dbname["tasks_collection"]

  #let's create two documents
  medicine_1 = {
      "medicine_id": "RR000123456",
      "common_name" : "Paracetamol",
      "scientific_name" : "",
      "available" : "Y",
      "category": "fever"
  }

  # Insert the documents
  collection_name.insert_one(medicine_1)

  api_urls = {
    'List': '/task-list',
    'Create': '/task-create',
    'Detail View': '/task-detail/<str:pk>',
    'Update': '/task-update',
    'Delete': '/task-delete',
  }
  return Response(api_urls)

@api_view(['GET'])
def taskList(req):
  tasks = getTasks()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def taskDetail(req):
  tasks = Task.objects.get()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

def getTasks():
  client = MongoClient('localhost', 27017)
  dbname = client['tasks']
  tasks_collection = dbname["tasks_collection"]
  all_tasks = tasks_collection.find()
  return all_tasks
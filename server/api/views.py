from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LogSerializer

from .models import Log


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Log':'/log-list/',
		'Detail View':'/log-detail/<str:pk>/',
		'Create':'/log-create/',
		'Delete':'/log-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def logList(request):
	logs = Log.objects.all().order_by('-id')
	serializer = LogSerializer(logs, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def logCreate(request):
	serializer = LogSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def logDelete(request, pk):
	log = Log.objects.get(id=pk)
	log.delete()

	return Response('Log succsesfully delete!')




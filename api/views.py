from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List': '/item-list/',
        'Detail View': '/item-detail/<str:pk>/',
        'Create': '/item-create/',
        'Update': '/item-update/<str:pk>/',
        'Delete': '/item-delete/<str:pk>/',
    }
    return Response(api_urls)



@api_view(['POST'])
def add_items(request):
	item = ItemSerializer(data=request.data)

	# validating for already existing data
	if Item.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


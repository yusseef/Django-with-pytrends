from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from .models import Region, Historical
from .serializers import RegionSerializer, HistoricalSerializer
from rest_framework import status

@api_view(['GET'])
def list_regions(request):
    try:
        regions = Region.objects.all()
    except regions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def list_historical(request):
    try:
        historical = Historical.objects.all()
    except historical.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HistoricalSerializer(historical, many=True)
        return Response(serializer.data)
        
def show_data(request):
    return render(request, 'index.html')

def show_data2(request):
    return render(request, 'map.html')
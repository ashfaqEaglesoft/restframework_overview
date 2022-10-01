from ast import Pass
import re
from urllib import response
from django.http import JsonResponse
from .models import drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from drinks import serializers

@api_view(['GET','POST'])

def drink_list(request, format=None):
    if request.method=='GET':
        dnk=drinks.objects.all()
        serializer=DrinkSerializer(dnk, many=True)
        return JsonResponse({'drinks':serializer.data})
    if request.method=='POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_details(request,id, format=None):
    try:
        drink=drinks.objects.get(pk=id)
    except drink.DoestNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        drink.delete()
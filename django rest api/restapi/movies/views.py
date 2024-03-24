from django.shortcuts import render
from .models import*
from rest_framework import viewsets
from .serializers import*


# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer
    
# ! create class for each categories such as actions , comedy etc etc , Not only 1 class ! # 

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieDataSerializer
    
    
class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieDataSerializer
    

class RomanticViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='romantic')
    serializer_class = MovieDataSerializer
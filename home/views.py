from django.shortcuts import render
from home.models import Car
from rest_framework import generics
from rest_framework import mixins
from home.api_file.serializer import CarSerializer

# Create your views here.

class Car_list (mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Car.objects.all ()
    serializer_class = CarSerializer

    def get (self , request , *args , **kwargs):
        return self.list (request , *args , **kwargs)
    
    def post (self , request , *args , **kwargs):
        return self.create (request , *args , **kwargs)
    
class Car_detail (mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Car.objects.all ()
    serializer_class = CarSerializer

    def get (self , request , *args , **kwargs):
        return self.retrieve (request , *args , **kwargs)
    
    def delete (self , request , *args , **Kwargs):
        return self.destroy (request , *args , **Kwargs)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as function (get, post, patch, put, delete'
            'is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manuallly to URLs',
        ]
        
        return Response({'message': 'Helllo!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello messagw with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )
            
    def put(self, request, pk=None):
        """Handle updating an object""" 
        return Response({'method': 'PUT'})  
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object""" 
        return Response({'method': 'PATCH'})    
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API View set"""
    
    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automaticalyy maps to URLs using routers',
            'Provides more functionality with less code'
        ]
        
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
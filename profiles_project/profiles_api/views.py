from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
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
    serializer_class = serializers.HelloSerializer
    
    
    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automaticalyy maps to URLs using routers',
            'Provides more functionality with less code'
        ]
        
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID""" 
        return Response({'http_method', 'GET'})
    
    def update(self, request, pk=None):
        """Handle Updating an object """ 
        return Response({'http_mehtod': "PUT"})
    
    def partial_update(self, request, pk=None):
        """Handle Updating part of an object """ 
        return Response({'http_mehtod': "PATCH"})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""    
        return Response({'htpp_method': 'DELETE'}) 
    
class UserProfileViewSet(viewsets.ModelViewSet):  
    """Handle creating and updating profiles""" 
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() 
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
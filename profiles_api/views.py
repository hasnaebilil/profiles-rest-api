from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloApiView(APIView):
    """Test API View."""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apitview': an_apiview})


    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})

        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""

        #serializer = serializers.HelloSerializer(data=request.data)

        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PUTCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

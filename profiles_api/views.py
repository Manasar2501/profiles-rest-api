from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
# Create your views here.

class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self,request,format = None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methdos as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})



    def post(self,request):
        '''create a hello message with our name'''
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):
        '''Handle updating an object'''
        return Response({'method':'PUT'})

    def patch(self, request,pk=None):
        ''' Handle a partial update of an object'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method':'DELETE'})

#----------------------------------------------------------------
class HelloViewSet(viewsets.ViewSet):
    '''TEst api viewset'''
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        '''return an hello message'''

        a_viewset = [
        'usese action(list,create,retrive,update,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality eith less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self,request):

        '''create a new helllo message'''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        '''handle getting an object by id'''
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        '''handle updating an object '''
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        '''handle updating part of an object'''
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        '''handle removing an object'''
        return Response({'http_method':'DELETE'})


#-------------------------------------------------------------
class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authenticationa_classes = (TokenAuthentication,)

    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

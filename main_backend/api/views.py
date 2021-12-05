from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main_backend.models import User, Event
from .serializers import UserSerializer, EventSerializer
from rest_framework.decorators import api_view

class UserListApiView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        maxId = User.objects.last().id + 1

        data = {
            'id': maxId,
            'name': request.data.get('name'),
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET',))
    def userById(request, userId):
        user = User.objects.filter(id=userId)
        newId = user.first().id
        serializer = UserSerializer(user[0], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventListApiView(APIView):
    def get(self, request, *args, **kwargs):
        event = Event.objects
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        maxId = Event.objects.last().id + 1

        data = {
            'id': maxId,
            'name': request.data.get('name'),
        }

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET',))
    def eventById(request, eventId):
        event = Event.objects.filter(id=eventId)
        newId = event.first().id
        serializer = EventSerializer(event[0], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

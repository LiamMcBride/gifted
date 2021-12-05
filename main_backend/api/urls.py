from django.conf.urls import url
from django.urls import path
from .views import UserListApiView, EventListApiView

urlpatterns = [
    path('users/', UserListApiView.as_view()),
    path('users/<str:userId>/', UserListApiView.userById),
    path('events/', EventListApiView.as_view()),
    path('events/<str:eventId>/', EventListApiView.eventById),
]
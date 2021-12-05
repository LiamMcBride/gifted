from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('api/', include('main_backend.api.urls')),
]
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Activity.models import UserDetail
from Activity.serializers import UserDetailsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailsSerializer
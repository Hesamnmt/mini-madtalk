from django.shortcuts import render
from rest_framework import generics  
from . import serializers
from .models import User

class AccountList(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer
    
    def get_queryset(self):
        user = self.request.user
        typee = self.request.GET.get('type')
        queryset = User.objects.all()
        queryset = queryset.filter(type=typee) if typee else queryset
        return queryset

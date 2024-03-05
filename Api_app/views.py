from django.shortcuts import render
from rest_framework import viewsets
from .models import Mainai
from .serializers import MainaiSerializer
# Create your views here.


class mainaiViewSet(viewsets.ModelViewSet):
    queryset = Mainai.objects.all()
    serializer_class = MainaiSerializer
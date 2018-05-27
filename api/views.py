from django.shortcuts import render
from rest_framework import generics

from todos import models
from . import serializers


class ListDeploy(generics.ListCreateAPIView):
    queryset = models.Deploy.objects.all()
    serializer_class = serializers.DeploySerializer


class DetailDeploy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Deploy.objects.all()
    serializer_class = serializers.DeploySerializer

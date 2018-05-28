from rest_framework import generics

from todos import models
from . import serializers
from todos import permissions


class ListDeploy(generics.ListCreateAPIView):
    queryset = models.Deploy.objects.all()
    serializer_class = serializers.DeploySerializer


class DeployDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthorOrReadOnly,)
    queryset = models.Deploy.objects.all()
    serializer_class = serializers.DeploySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.Deploy.objects.filter(author=user)

# class DetailDeploy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Deploy.objects.all()
#     serializer_class = serializers.DeploySerializer

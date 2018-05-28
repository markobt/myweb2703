from rest_framework import serializers
from todos import models


class DeploySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deploy
        fields = ('id', 'author', 'name', 'project', 'version', 'comment', 'created_at')

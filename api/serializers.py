from rest_framework import serializers
from todos import models


class DeploySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'project',
            'author',
            'comment',
        )
        model = models.Deploy

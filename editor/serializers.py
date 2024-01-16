from rest_framework import serializers
from . import models

class EditorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Editor
        fields = '__all__'
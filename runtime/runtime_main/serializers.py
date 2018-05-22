from rest_framework import serializers
from .models import UserInfo
from rest_framework import viewsets

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'

class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': UserInfoSerializer
    }

    def get_serializer_class(self, *args, **kwargs):
        return self.serializers.get(self.action, self.serializers['default'])




class PredictionSerializer(serializers.Serializer):

    values = serializers.FloatField()
from rest_framework import serializers
<<<<<<< HEAD
from .models import UserInfo
from rest_framework import viewsets
=======
from .models import UserInfo, MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

>>>>>>> teraz

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
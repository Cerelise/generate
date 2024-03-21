from rest_framework import serializers

from .models import Origin, Result
from accounts.serializers import UserSerializer


class ResultSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Result
        fields = ('modified_pic','like_count','created_by')


class OriginSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()
    class Meta:
        model = Origin
        fields = ('id','name','result','picture','created_at','modified_at','is_modify','created_by')

    def get_result(self,instance):
        # print(instance.id)
        result = Result.objects.filter(origin=instance.id).first()
        if result:
           return 'http://127.0.0.1:8000/media/' + str(result.modified_pic)
        return 'None'

    def to_representation(self, value):
        data = super().to_representation(value)
        data['picture'] = 'http://127.0.0.1:8000' + data['picture']
        return data
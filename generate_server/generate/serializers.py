from accounts.serializers import UserSerializer
from rest_framework import serializers

from .models import Origin, Result


class ResultSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Result
        fields = ('id','modified_pic','like_count','created_by')

    def to_representation(self, value):
        data = super().to_representation(value)
        data['modified_pic'] = 'http://127.0.0.1:8000' + data['modified_pic']
        return data


class OriginSerializer(serializers.ModelSerializer):
    # result = serializers.SerializerMethodField()
    result = serializers.ReadOnlyField(source=Result.objects)
    class Meta:
        model = Origin
        fields = ('id','name','result','picture','created_at','modified_at','is_modify','created_by')

    # 获取result表的字段
    def get_result(self,instance):
        # print(instance.id)
        result = Result.objects.filter(origin=instance.id).first()
        if result:
           return 'http://127.0.0.1:8000/media/' + str(result.modified_pic)
        return 'None'
    
    # picture 原图地址自定义返回
    def to_representation(self, value):
        data = super().to_representation(value)
        data['picture'] = 'http://127.0.0.1:8000' + data['picture']
        return data
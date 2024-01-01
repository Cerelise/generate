from rest_framework import serializers

from .models import Original,Result

class OriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Original
        fields = ('id','name','origin_pic','created_at','modified_at','is_modify','created_by')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id','modified_pic','created_by','created_at')
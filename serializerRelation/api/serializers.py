from  rest_framework import serializers
from .models import Singer,Song
class SongSerializer(serializers.Serializer):
    class Meta:
        model=Song
        fields='__all__'

class SingerSerializer(serializers.Serializer):
    song=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Singer
        fields='__all__'
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(seelf,instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.roll=validated_data.get('roll', instance.roll)
        instance.city=validated_data.get('city', instance.city)
        instance.save()
        return instance

    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("seat fulll")
        return value
from rest_framework import serializers

class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)

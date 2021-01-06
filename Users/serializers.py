from rest_framework import serializers

class NormalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    username = serializers.CharField()
    address = serializers.CharField()
    mobileNumber = serializers.CharField()
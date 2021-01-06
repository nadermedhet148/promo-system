from rest_framework import serializers
from Users.serializers import NormalSerializer
class PromoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    promoType = serializers.CharField(max_length=200)
    promoCode = serializers.IntegerField()
    creationTime  = serializers.DateField()
    startTime = serializers.CharField()
    endTime = serializers.CharField()
    promoAmount = serializers.IntegerField()
    isActive = serializers.BooleanField()
    description = serializers.CharField()
    normalUser = NormalSerializer()
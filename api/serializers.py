from rest_framework import serializers
from .models import booking

class BookingSerializer(serializers.Serializer):
    bookingid = serializers.IntegerField()
    userid_id=serializers.IntegerField()
    carid_id=serializers.IntegerField()
    startdate=serializers.DateTimeField()
    returndate=serializers.DateTimeField()
    totalprice=serializers.IntegerField()
    extratime=serializers.DateTimeField()
    ismanual=serializers.BooleanField()

    def create(self, validated_data):
        return booking.objects.create(**validated_data)
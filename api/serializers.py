from rest_framework import serializers
from .models import booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields='__all__'
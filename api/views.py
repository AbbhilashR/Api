from django.shortcuts import render
from rest_framework import generics
from .models import booking,car,user
from .serializers import BookingSerializer

class BookingAPIView(generics.ListAPIView):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
# Create your views here.

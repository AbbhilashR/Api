# from django.shortcuts import render
# from rest_framework import generics
# from .models import booking,car,user
# from .serializers import BookingSerializer

# class BookingAPIView(generics.ListAPIView):
#     queryset = booking.objects.all()
#     serializer_class = BookingSerializer
# # Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import booking
from .serializers import BookingSerializer

class BookingView(APIView):
    def get(self,request):
        bookings=booking.objects.all()
        serializer=BookingSerializer(bookings,many=True)
        return Response({"bookings":serializer.data})

    def post(self,request):
        bookings=request.data.get('booking')
        print(bookings)
        serializer=BookingSerializer(data=bookings)
        if serializer.is_valid(raise_exception=True):
            booking_saved=serializer.save()
        return Response({"success":"Booking '{}' created successfully".format(booking_saved.bookingid)})

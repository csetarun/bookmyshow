from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class TheatreList(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

    def get_queryset(self):
        queryset = self.queryset
        city = self.request.query_params.get('city', None)
        if city:
            queryset = queryset.filter(city=city)
        return queryset

class ShowList(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    def get_queryset(self):
        queryset = self.queryset
        movie = self.request.query_params.get('movie', None)
        if movie:
            queryset = queryset.filter(movie__name=movie)
        return queryset
            

class MoviesList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        city = self.request.query_params.get('city', None)
        if city:
            queryset = queryset.filter(show__theatre__city=city)
        return queryset

class SeatList(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        show = self.request.query_params.get('show', None)
        if show:
            booked_seats = BookedSeat.objects.all().values_list('seat')
            queryset = queryset.filter(show=show).exclude(id__in=booked_seats)
        return queryset

class BookingList(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookedSeatList(viewsets.ModelViewSet):
    queryset = BookedSeat.objects.all()
    serializer_class = BookedSeatSerializer
    permission_classes = [IsAuthenticated]
from .models import *
from rest_framework import serializers

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='movie.name',read_only=True)
    theatre_name = serializers.CharField(source='theatre.name', read_only=True)
    class Meta:
        model = Show
        fields = '__all__'
        # exclude = ['movie','theatre']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = '__all__'
from rest_framework import serializers
from .models import Movie, Customer, Places, Ticket

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'
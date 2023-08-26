from rest_framework import generics
from .models import Movie, Customer, Places, Ticket
from .serializers import MovieSerializer, CustomerSerializer, PlacesSerializer, TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    
    def get(self, request):
        data = {
            "message": "Welcome to the CinemaProject",
        }
        return Response(data)

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

class PlacesList(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer

class PlacesDetail(generics.RetrieveAPIView):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer

class MovieCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TicketCreate(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PlacesCreate(generics.CreateAPIView):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
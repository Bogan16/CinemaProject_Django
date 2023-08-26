from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/create/', MovieCreate.as_view(), name='movie-create'),
    path('movies/<slug:slug>/', MovieDetail.as_view(), name='movie-detail'),

    path('tickets/', TicketList.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreate.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),

    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customers/<int:id>/', CustomerDetail.as_view(), name='customer-detail'),

    path('places/', PlacesList.as_view(), name='places-list'),
    path('places/create/', PlacesCreate.as_view(), name='places-create'),
    path('places/<int:pk>/', PlacesDetail.as_view(), name='places-detail'),  
]
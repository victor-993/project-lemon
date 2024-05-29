from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu, User
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.
def index(request):
    home = "#"
    return render(request, "index.html")

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

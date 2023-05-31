from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class AppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

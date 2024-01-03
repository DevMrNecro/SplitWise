from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import User, Room, ElectricityBill, ExpenseParticipants
from .serializers import UserSerializer, RoomSerializer, ElectricityBillSerializer, ExpenseParticipantsSerializer, UserViewSerializer, RoomViewSerializer, ElectricityBillViewSerializer, ExpenseParticipantsViewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination = []

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination = []

class ElectricityBillViewSet(viewsets.ModelViewSet):
    queryset = ElectricityBill.objects.all()
    serializer_class = ElectricityBillSerializer
    pagination = []

class ExpenseParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ExpenseParticipants.objects.all()
    serializer_class = ExpenseParticipantsSerializer
    pagination = []

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    pagination = []

class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomViewSerializer
    pagination = []

class ElectricityBillListAPIView(generics.ListAPIView):
    queryset = ElectricityBill.objects.all()
    serializer_class = ElectricityBillSerializer
    pagination = []

class ElectricityBillListAPIView(generics.ListAPIView):
    queryset = ElectricityBill.objects.all()
    serializer_class = ElectricityBillViewSerializer
    pagination = []

class ExpenseParticipantListAPIView(generics.ListAPIView):
    queryset = ElectricityBill.objects.all()
    serializer_class = ExpenseParticipantsViewSerializer
    pagination = []
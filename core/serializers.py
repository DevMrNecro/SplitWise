from rest_framework import serializers
from .models import User, Room, ElectricityBill, ExpenseParticipants

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ElectricityBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityBill
        fields = '__all__'

class ExpenseParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseParticipants
        fields = '__all__'

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoomViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ElectricityBillViewSerializer(serializers.ModelSerializer):
    room_no = RoomSerializer()
    payees = UserSerializer(many=True)
    paid_by = UserSerializer()
    splited_amongst = UserSerializer(many=True)

    class Meta:
        model = ElectricityBill
        fields = '__all__'

class ExpenseParticipantsViewSerializer(serializers.ModelSerializer):
    electricity_bill = ElectricityBill()
    payee_user = UserSerializer()
    participant = UserSerializer(many=True)
    
    class Meta:
        model = ExpenseParticipants
        fields = '__all__'
from django.db import models
import uuid
from django.core.exceptions import ValidationError

#User details model 
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    split_share = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    pending_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#pending 
EXPENSE_TYPE = [
    ('EQUAL', 'EQUAL'),
    ('EXACT', 'EXACT'),
    ('PERCENT', 'PERCENT')
    ]

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    room_no = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.room_no)

class ElectricityBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    payees = models.ManyToManyField(User, related_name='payees')
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    splited_amongst = models.ManyToManyField(User, blank=True, related_name='splited_amongst')
    expense_type = models.CharField(max_length=10, blank=True, null=True)
    remaining_ammount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    deadline = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        max_participants = 3
        if self.payees.count() > max_participants:
            raise ValidationError({'payees':
                [f'You can only add payees upto {max_participants}.']
                })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.room_no.room_no)

class ExpenseParticipants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    electricity_bill = models.ForeignKey(ElectricityBill, on_delete=models.CASCADE, blank=True, null=True)
    payee_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payee')
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    participant = models.ManyToManyField(User, related_name='participants')
    deadline_to_payees = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.payee_user.name
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ExpenseParticipants, ElectricityBill, User
from .utils import send_email
from requests import request

@receiver(post_save, sender=ExpenseParticipants)
def AfterBillGenerated(sender, instance, created, **kwargs):
    if created or not created:
        print('POST SIGNAL --> CREATED')

        #here we're getting ExpenseParticpants obj to update the Electricity's obj values, which can be used later to see the complete info of ppl paying the money in splits.

        expense_obj=ExpenseParticipants.objects.filter(payee_user=instance.payee_user)[0]
        bill_obj=ElectricityBill.objects.filter(id=expense_obj.electricity_bill.id)[0]
        bill_obj.paid_by = expense_obj.payee_user
        bill_obj.is_paid = True
        bill_obj.splited_amongst.add(*[x for x in expense_obj.participant.all()])
        bill_obj.expense_type = expense_obj.expense_type
        bill_obj.remaining_ammount = bill_obj.bill_amount - expense_obj.amount
        bill_obj.save()

        queryset = expense_obj.participant.all().exclude(id=instance.payee_user.id)

        total_participants = expense_obj.participant.all()
        share_amount = None
        for i in range(len(queryset)):
            print('queryset', queryset[i])
            obj=User.objects.filter(id=queryset[i].id)[0]
            obj.pending_amount = (bill_obj.bill_amount - bill_obj.remaining_ammount) / len(total_participants)  
            obj.split_share = obj.pending_amount
            obj.deadline=expense_obj.deadline_to_payees
            share_amount=(bill_obj.bill_amount - bill_obj.remaining_ammount) / len(total_participants)
            obj.save()
        
        #Explicitly saving payee user's pending_amount=0 since he is paying the amount.
        #split_share shows the how much the shared ammount been divided to each one.
        payee_user_obj = User.objects.filter(id=instance.payee_user.id)[0]
        payee_user_obj.split_share = share_amount
        payee_user_obj.pending_amount = 0.0
        payee_user_obj.save()

        lst=[x.email for x in total_participants]
        for obj in total_participants:
            subject="You've been added to an expense"
            message=f'Electricity bill ID:"{expense_obj.electricity_bill.id}", Your new expense has just created by {obj.name} from following id no:"{obj.id}", Your bill has been splitted by amount ₹{obj.split_share} for each one and Your pending amount is now: ₹{obj.pending_amount}, Which you can must pay before your deadline - {obj.deadline}.'
            send_email(request, subject, message, lst)
    
        
        
            
        



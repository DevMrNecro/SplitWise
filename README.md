Core APP is the only and main application and responsible for all the apis and functionalities.

Apologies:-
EXPENSE_TYPE is not yet integrated
EMAIL SCHEDULER is not working as async yet

Working:
--> User model is responsible for holding user related data and some fields are not meant to be filled initiall like; split_share , pending_amount, deadline. This data will be later get added dynamically when any Expense object is made.
--> Room model is for making rooms on which an user can create an electricty_bill obbject.
--> ElectricityBill model is for creating bill to later create an expense for it, many fields will not be filled initially like; paid_by, splited_amongst, expense_type, remaining_ammount, is_paid. This data will be filled dynamically when any expense is made.
--> ExpenseParticipants model is for creating the expense; all the fields will be fiiled fully, Deadline field is the field by which the user who is paying the money can set a period of time to get money returned from the payees he is splitting, which later updates this info at User model.

==> In User model we can check whether which user has money pending and also the last shared split amount.
==> In ElectricityBill user who is creating the bill can check always whther the money is been paid or not and can see to whom all its being splitted and also cans see the remaining amount if in case any payer is not putting the full amount.
==> In ExpenseParticipants user can submit the amount, this amount will be paid by the single payer on behalf of all payees.


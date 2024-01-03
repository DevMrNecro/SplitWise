from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoomViewSet, ElectricityBillViewSet, ExpenseParticipantsViewSet, UserListAPIView, RoomListAPIView, ElectricityBillListAPIView, ExpenseParticipantListAPIView

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'room', RoomViewSet)
router.register(r'electricity-bill', ElectricityBillViewSet)
router.register(r'expense-participants', ExpenseParticipantsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-view', UserListAPIView.as_view(), name='user-name'),
    path('room-view', RoomListAPIView.as_view(), name='room-view'),
    path('electricity-bill-view', ElectricityBillListAPIView.as_view(), name='electricity-bill-view'),
    path('expense-participants-view', ExpenseParticipantListAPIView.as_view(), name='expense-participants-view'),
]

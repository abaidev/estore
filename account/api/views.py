from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from account.models import Customer, User
from .serializers import (CustomerProfileSerializer, CustomerListSerializer,
                          CustomerCreateSerializer,)
from .permissions import AllowAny, IsCustomerOrReadOnly, IsAdminUser


class CustomerProfileAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerProfileSerializer
    queryset = Customer.objects.all()
    lookup_field = 'user'
    permission_classes = [IsCustomerOrReadOnly]

    def get_object(self):
        user = User.objects.get(username=self.kwargs['user'])
        return self.queryset.get(user=user)

class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()
    permission_classes = [AllowAny]


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerCreateSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAdminUser]
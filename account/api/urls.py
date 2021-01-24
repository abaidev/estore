from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (CustomerProfileAPIView, CustomerListAPIView,
                    CustomerCreateAPIView)

app_name = 'account-api'

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view(), name='customers'),
    path('customers/<user>/', CustomerProfileAPIView.as_view(), name="profile"),
    path('create/', CustomerCreateAPIView.as_view(), name='create'),
    path('auth/token/', obtain_jwt_token, name='auth-token'),
]
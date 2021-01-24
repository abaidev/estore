from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (LoginView,
                    LogoutView,
                    CustomerCreateView,
                    CustomerProfileView,
                    CustomerDeleteView,
                    CusPasswordResetView,
                    CusPasswordResetDoneView,
                    CusPasswordResetConfirmView,
                    CusPasswordResetCompleteView,
                    )

app_name = 'account'

urlpatterns = [
    path('profile/<str:username>/', CustomerProfileView.as_view(), name="profile"), # USER PROFILE (DETAIL UPDATE VIEW).
    path('delete/', CustomerDeleteView.as_view(), name="profile-delete"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', CustomerCreateView.as_view(), name='register'),
    path('password_reset/', CusPasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', CusPasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', CusPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', CusPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
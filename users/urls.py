from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, OTPVerificationView, LoginView

app_name='users'
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('verify/', OTPVerificationView.as_view(), name='otp_verification'),
]

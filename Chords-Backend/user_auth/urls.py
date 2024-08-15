from django.urls import path
from user_auth.views import PasswordResetView, UserLoginView, UserRegistrationView 


urlpatterns = [
    path('signup', UserRegistrationView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='signin'),
    # path('sociallogin/',SocialLoginView.as_view() , name="SocialLoginView"),
    path('reset-password', PasswordResetView.as_view(), name='reset-password'),
]

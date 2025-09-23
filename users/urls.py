from django.urls import path
from .views import LoginUser, LogoutUser, RegisterUser, PasswordChangeUser
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('password-change/', PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
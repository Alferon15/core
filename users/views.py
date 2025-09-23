from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.edit import CreateView
from .forms import LoginUserForm, RegisterUserForm, PasswordChangeUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:home')


class LogoutUser(LogoutView):
    template_name = "registration/logged_out.html"


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class PasswordChangeUser(PasswordChangeView):
    form = PasswordChangeUserForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')
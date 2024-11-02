from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from .forms import CustomUserForm
from django.urls import reverse_lazy
# Create your views here.


class CustomUserLoginView(LoginView):
    template_name = 'userauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        #check if there is a 'next' url, if yes, redirect the user
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('main')


class CustomUserSignupView(CreateView):
    template_name = 'userauth/signup.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('login')


class CustomLogoutView(LogoutView):
    next_page = 'login'
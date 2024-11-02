from django.urls import path
from .views import CustomUserLoginView,CustomLogoutView,CustomUserSignupView
urlpatterns = [
    path('login/',CustomUserLoginView.as_view(),name='login'),
    path('logout',CustomLogoutView.as_view(),name='logout'),
    path('signup/',CustomUserSignupView.as_view(),name='signup')
]
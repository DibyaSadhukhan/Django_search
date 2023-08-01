from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('login',views.login,name='Login'),
    path('logout',views.logout,name='Logout'),
    path('signup',views.signup,name='Register'),
]
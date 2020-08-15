from password_generator.views import *
from django.urls import path



urlpatterns = [ 
    # path('', home, name='welcome-page'),
    path('password_generator', home, name='password_home'),
    path('password/', password, name='password'),
    path('about/', about, name='about')


]
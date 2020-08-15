from django.urls import path
from portfolio.views import *

urlpatterns =[
    path('', portfolio, name='my_portfolio')
]


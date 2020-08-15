from django.shortcuts import render
from portfolio.models import *
# Create your views here.

def portfolio(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/portfolio.html',locals())
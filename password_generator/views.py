from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def password_home(request):
	return render(request, 'password_generator/password_home.html')


def about(request):
	return render(request, 'password_generator/about.html')

def password(request):
	length 		= int(request.GET.get('length',5))

	alpha 		= 'abcdefghijklmnopqrestuvwxyz'
	character	= list(alpha.lower())

	if request.GET.get('uppercase'):
		character.extend(list(alpha.upper()))

	if request.GET.get('numbers'):
		character.extend(list('0123456789'))

	if request.GET.get('special'):
		character.extend(list('!@#$&*?'))

	thepassword=''
	# import ipdb;ipdb.set_trace()
	for i in range(length):
		thepassword += random.choice(character)

	return render(request,'password_generator/password.html',{'thepassword':thepassword, 'path':request.get_full_path()})
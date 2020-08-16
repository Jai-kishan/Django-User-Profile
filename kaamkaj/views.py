from django.db import IntegrityError
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from .forms import TodoForm
from .models import *
# Create your views here.

@login_required
def kaamkaj(request):
	return render(request,'kaamkaj/kaamkaj_home.html',locals())


@login_required
def kaam_list(request):
	todos  = KaamKaj.objects.filter(user=request.user, complete_date__isnull=True).order_by('-created')
	return render(request,'kaamkaj/current_kaam.html',locals())

# def signup_user(request):
# 	if request.method == "GET":
# 		return render(request,'todos/signup.html',{'form':UserCreationForm})
# 	else:
# 		if request.POST.get('password1') == request.POST.get('password2'):
# 			try:
# 				user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password1'))
# 				user.save()
# 				login(request,user)
# 				return redirect('home')

# 			except IntegrityError:
# 				return render(request,'todos/signup.html',{'form':UserCreationForm, 'error':"That username has already been taken. Please choose a new username."})
# 		else:
# 			return render(request,'todos/signup.html',{'form':UserCreationForm, 'error':"Password didn't match"})
		
# @login_required
# def logout_user(request):
# 	if request.method == "POST":
# 		logout(request)
# 		return redirect('login')


# def login_user(request):
# 	if request.method == "GET":
# 		return render(request,'todos/login.html',{'form':AuthenticationForm})
# 	else:
# 		user = authenticate(request,username=request.POST.get('username'), password=request.POST.get('password'))
# 		if user is None:
# 			return render(request,'todos/login.html',{'form':AuthenticationForm, 'error':"username and password didn't matched"})
# 		else:
# 			login(request,user)
# 			return redirect('home')

@login_required
def create_kaam(request):
	# import ipdb; ipdb.set_trace()
	if request.method == 'GET':
		return render(request,'kaamkaj/create_kaam.html', {'form':TodoForm})
	else:
		try:
			form 		= TodoForm(request.POST)
			new_todo	=form.save(commit=False)
			new_todo.user = request.user
			new_todo.save()
			return redirect('kaamkaj_list')
		except ValueError:
			return render(request,'kaamkaj/create_kaam.html', {'form':TodoForm, 'error':'Bad data passend in. Try again'} )

@login_required
def kaamkaj_details(request,todo_id):
	# import ipdb;ipdb.set_trace()
	todo = get_object_or_404(KaamKaj, id=todo_id, user=request.user)
	if request.method == "GET":
		form = TodoForm(instance=todo)
		return render(request,'kaamkaj/kaamkaj_details.html', {'todo':todo,'form':form})
	else:
		try:
			form = TodoForm(request.POST, instance=todo)
			form.save()
			return redirect('kaamkaj_list')
		except ValueError:
			return render(request,'kaamkaj/kaamkaj_details.html', {'todo':todo, 'form':form, 'error':'Bad Info'} )

@login_required
def kaamkaj_complete(request,todo_pk):
	todo = get_object_or_404(KaamKaj, id=todo_pk, user=request.user)
	if request.method == 'POST':
		todo.complete_date = timezone.now()
		todo.save()
		return redirect('kaamkaj_list')
		
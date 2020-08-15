from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user_profile.tokens import account_activation_token
from django.contrib.auth import login, authenticate,logout
from user_profile.forms import *
from user_profile.models import * 
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html',locals())


@login_required
def home(request):
    return render(request, 'home.html',locals())    

def user_signup(request):    
    if request.method == 'POST':
        form            = SignUpForm(request.POST)
        check =''
        if form.is_valid():
            fname           = request.POST.get('firstname')
            lname           = request.POST.get('lastname')
            email           = request.POST.get('email')
            birth_date      = request.POST.get('date_of_birth')
            pwd             = request.POST.get('password1')

            try:
                check       = User.objects.get(username=email,email=email)
            except:
                pass

            if not check:   
                userobj = User.objects.create_user(username=email.lower(),email=email,password=pwd)
                userobj.first_name=fname
                userobj.last_name=lname
                userobj.is_active = True
                userobj.save()

                profile_data = UserProfile.objects.create(user=userobj,birth_date=birth_date)
                user         = authenticate(username=userobj.username, password=pwd)
                login(request, user)
                return redirect('welcome-page')                 
            else:
                msg = "Email already exists"
                form = SignUpForm(request.POST, request.FILES)
        else:
            form = SignUpForm(request.POST, request.FILES)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user        = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome-page')
        else:
            msg='Invalid Username and password '
    return render(request,'registration/login.html',locals())


def user_logout(request):
    logout(request)
    return redirect('login')


def change_password(request):
    # import ipdb;ipdb.set_trace()
    user = request.user
    model = "old"

    if request.POST:
       # Handle post request
       old = request.POST["old_password"]
       new = request.POST['new_password']
       conf = request.POST['confirm_password']

       e1 = '' if new else "Password can't be left blank"
       e3 = '' if old else "Password can't be left blank"
       e2 = '' if conf else "Password can't be left blank"

       if request.user != authenticate(username=request.user.username, password=old):
           e3 = " Incorrect password"
       elif len(new) < 6 and new:
           e1 = "Password should be atleast 6 charactors"
       elif conf != new:
           e2 = "Passwords doesn't match, please try again."

       elif not any([e1, e2, e3]):
           user.set_password(new)
           user.save()
           return HttpResponseRedirect(
               "/login/"
           )
    # Render to template
    return render(request, 'registration/change_password.html', locals())

@login_required
def user_profile(request):
    try:
        user_data= UserProfile.objects.get(user=request.user.id)
    except UserProfile.DoesNotExist:
        user =None
    return  render(request,'profile/user_profile.html',locals())


@login_required
def edit_user_profile(request,pk):
    user = User.objects.get(id=pk)    
    usr = UserProfile.objects.get(user=user)

    if request.method== "POST":
        form = UserProfileEditForm(request.POST,request.FILES)
        form.actual_user = request.user
        if form.is_valid():
            email = request.POST.get('email')
            check = User.objects.filter(email=email).exclude(id=pk).exists()
            if not check:
                user.first_name      = request.POST.get('first_name')               
                user.email = email
                user.save()
                
                birth_date      = request.POST.get('birth_date')
                if birth_date != '':
                    usr.birth_date = birth_date
                
                contact         = request.POST.get('contact')
                if contact != '':
                    usr.contact = contact
                     
                secondary_email = request.POST.get('secondary_email')
                usr.secondary_email = secondary_email

                gender          = request.POST.get('gender')
                if gender != '':
                    usr.gender = gender
                    
                # import ipdb;ipdb.set_trace()

                try:
                    usr.profile_pic     = request.FILES['profile_pic']
                except MultiValueDictKeyError:
                    pass

                usr.save()
                return redirect('profile')
                
            else:
                form = UserProfileEditForm(request.POST)
                error = "Email already exists in our database"
        else:
            form = UserProfileEditForm(request.POST)
    else:
        form = UserProfileEditForm(initial={
            'username':usr.user.username,'first_name':usr.user.first_name,'email':usr.user.email,
            'secondary_email':usr.secondary_email,'gender':usr.gender,'birth_date':usr.birth_date,
            'contact':usr.contact,'last_name':usr.user.last_name,
            'profile_pic':usr.profile_pic.url,
          })
    return render(request,'profile/edit_user_profile.html', locals())
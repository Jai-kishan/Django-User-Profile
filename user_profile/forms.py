from django import forms
from django.contrib.auth.models import User
from .models import *

class SignUpForm(forms.Form):
    firstname       = forms.RegexField(label="First name*", max_length=30,regex=r'^[a-zA-Z0-9 ]+$',widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    lastname        = forms.RegexField(label="Last name", max_length=30,regex=r'^[a-zA-Z ]+$',required=False ,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email           = forms.EmailField(label = 'Email* ',max_length=80,widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True,help_text='Required. Inform a valid email address.')
    date_of_birth   = forms.DateField(label = 'Birthday',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%d.%m.%Y'))
    password1       = forms.CharField(label="Password*", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2       = forms.CharField(label="Password verify*", widget=forms.PasswordInput(attrs={'class' : 'form-control'}), help_text = "Enter the same password for Verification.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email


    def clean_username(self):
        # -----clean username---------#
        # raise error if user with that username already exists
        # ----------ends------------------#
        username = self.cleaned_data["email"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_password2(self):
        # ---clean password------------# 
        # password1 and password2 are cleaned data
        # raise validation error if two  password fields didn't match
        # -------ends--------------------#

        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

SEX = ((0,'Male'),(1,'Female'),(2,'Other'))
class UserProfileEditForm(forms.Form):
    first_name      = forms.RegexField(label="First name*",     max_length=30,regex=r'^[a-zA-Z ]+$',widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    email           = forms.EmailField(label = 'Email* ',max_length=80,widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True,help_text='Required. Inform a valid email address.')
    contact         = forms.RegexField(label = 'Mobile', max_length=10, required=False,regex=r'^[0-9 ]+$',widget=forms.TextInput(attrs={'class' : 'form-control'}))
    secondary_email = forms.EmailField(label = 'Secondary Email ',max_length=80,widget=forms.TextInput(attrs={'class' : 'form-control'}),required=False,help_text='Required. Inform a valid email address.')
    gender          = forms.ChoiceField(label='', choices=SEX, widget=forms.Select(attrs={'class':'form-control'}))
    birth_date      = forms.DateField(label = 'Birth Date* ', required=False,widget=forms.TextInput(attrs={'class':"form-control"}))        
    # profile_pic     = forms.FileField(label="Image",widget=forms.ClearableFileInput(attrs={'class':"upload-btns-wrapper btns",'style': 'margin-top: 7px;'}),required=False)
    profile_pic     = forms.FileField()
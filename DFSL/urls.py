"""DFSL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_profile.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', user_login),
    path('', home, name='welcome-page'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login,name='login'),
    path('logout/', user_logout,name='logout'),
    path('change-password/', change_password, name='change-password'),
    path('profile/', user_profile, name = 'profile'),
    path('edit_profile/<int:pk>/', edit_user_profile, name = 'edit-profile'),

    path('password/reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name="password-reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'registration/password_reset_done.html'),name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name= 'registration/password_reset_complete.html'),name='password_reset_complete'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
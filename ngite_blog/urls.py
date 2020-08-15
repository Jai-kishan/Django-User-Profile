from django.urls import path
from ngite_blog.views import *

app_name ='blog'

urlpatterns = [
    path('', my_blogs, name='all_blog'),
    path('<int:blog_id>/', blog_deatail, name='blog_detail'),
]
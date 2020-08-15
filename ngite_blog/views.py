from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def my_blogs(request):
	blogs  = Blog.objects.order_by('-created')
	return render(request, 'ngite_blog/blogs.html',locals())


def blog_deatail(request,blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'ngite_blog/details.html',locals())
from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.

def posts_list(request):
	posts = Posts.objects.all()
	n = 'MaG'
	return render(request, 'blog/index.html', context = {'posts': posts})

def post_detail(request, slug):
	post = Posts.objects.get(slug__iexact = slug)
	return render(request, 'blog/post_detail.html', context = {'post': post})


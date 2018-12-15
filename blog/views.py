from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View

from .utils import * 
from .models import Posts, Tag
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

def posts_list(request):
	posts = Posts.objects.all()
	n = 'MaG'
	return render(request, 'blog/index.html', context = {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
	model = Posts
	template = 'blog/post_detail.html'
	

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = TagForm
	template = 'blog/tag_create.html'
	raise_exception = True
	
class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'blog/tag_update_form.html'
	raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'blog/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exception = True			

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form_model = PostForm
	template = 'blog/post_create_form.html'
	raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Posts
	model_form = PostForm
	template = 'blog/post_update_form.html'
	raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Posts
	template = 'blog/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exception = True

class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context = {'tags': tags})




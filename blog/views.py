from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .utils import * 
from .models import Posts, Tag
from .forms import TagForm, PostForm

def posts_list(request):
	posts = Posts.objects.all()
	n = 'MaG'
	return render(request, 'blog/index.html', context = {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
	model = Posts
	template = 'blog/post_detail.html'
	

class TagCreate(ObjectCreateMixin, View):
	form_model = TagForm
	template = 'blog/tag_create.html'
	
class TagUpdate(View):
	def get(self, request, slug):
		tag = Tag.objects.get(slug__iexact=slug)
		bound_form = TagForm(instance=tag)
		return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

class PostCreate(ObjectCreateMixin, View):
	form_model = PostForm
	template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'
	



def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context = {'tags': tags})




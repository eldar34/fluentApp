from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .utils import ObjectDetailMixin 
from .models import Posts, Tag
from .forms import TagForm

# Create your views here.

def posts_list(request):
	posts = Posts.objects.all()
	n = 'MaG'
	return render(request, 'blog/index.html', context = {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
	model = Posts
	template = 'blog/post_detail.html'
	# def get(self, request, slug):
	# 	post = get_object_or_404(Posts, slug__iexact=slug)
	# 	return render(request, 'blog/post_detail.html', context = {'post': post})

class TagCreate(View):
	def get(self, request):
		form = TagForm()
		return render(request, 'blog/tag_create.html', context={'form': form})

	def post(self, request):
		bound_form = TagForm(request.POST)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)
		return render(request, 'blog/tag_create.html', context = {'form': bound_form})

class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'
	# def get(self, request, slug):
	# 	tag = get_object_or_404(Tag, slug__iexact = slug)
	# 	return render(request, 'blog/tag_detail.html', context= {'tag': tag})



def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context = {'tags': tags})




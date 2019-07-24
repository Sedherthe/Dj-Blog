from django.shortcuts import render
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post

# Lets assume we are getting data from the database for now
posts = [
	{
		'title' : 'Blog Post 1',
		'author' : 'Soma',
		'content' : 'This is my first blog.',
		'date_published' : '10/07/1999',
	},
	{
		'title' : 'Blog Post 2',
		'author' : 'Siddhartha',
		'content' : 'This is my second Blog Post',
		'date_published' : '11/07/1999',
	}
]

context = {
		'posts' : Post.objects.all()
	}

# Create your views here.
def home(request):
	print(f"response is {request}")
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post # The model on which it queries
	template_name = 'blog/home.html' # Default path where it searches for template is ; blog/post_listview.html
	context_object_name = 'posts' # object_list is the default name which it gives to the key of the dict.
	ordering = ['-date_published']

#To add login functionality to class views.Use mixins
class PostDetailView(DetailView):

	model = Post
	# By default it looks for <app>/<model>_<viewtype>.html
	# So : blog/Post_detail.html
	# Object is the default context dict key.

class PostCreateView(LoginRequiredMixin, CreateView):

	model = Post
	fields = ['title', 'content']

	# Success url can also be used to just redirect.

	# As author cannot be null. We will give author as the user and
	# then validate/check the form 
	def form_valid(self, form):
		print(type(self), "super is ", super())
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

	 model = Post
	 fields = ['title', 'content']

	 def form_valid(self, form):
	 	form.instance.author = self.request.user
	 	return super().form_valid(form)

	 def test_func(self):
	 	# We can the current object using the below method
	 	# of UpdateView.
	 	post = self.get_object()
	 	if self.request.user == post.author:
	 		return True
	 	return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

	# Template will be post_confirm_delete.html	
	model = Post

	success_url = '/blog' # Redirection for success

	def test_func(self):
		post = self.get_object()
		if post.author == self.request.user:
			return True
		return False


# View function to handle about page in blog
def about(request):
	print(f'blog-about request is {request}')
	return render(request, 'blog/about.html', {'title' : 'About'})

def ddown(request):
	print(f'blog-about request is {request}')
	return render(request, 'blog/dropdown.html')

def nav(request):
	return render(request, 'blog/nav.html')

def navbar(request):
	return render(request, 'blog/blog-navbar.html')

def collapse(request):
	return render(request, 'blog/collapse.html')

def article(request):
	return render(request, 'blog/article.html', context)

def form(request):
	return(render(request, 'blog/form.html'))
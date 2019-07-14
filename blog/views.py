from django.shortcuts import render

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
		'posts' : posts
	}

# Create your views here.
def home(request):
	print(f"response is {request}")
	return render(request, 'blog/home.html', context)

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
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('ddown/', views.ddown, name='blog-ddown'),
	path('nav/', views.nav, name='blog-nav'),
	path('navbar/', views.navbar, name='blog-navbar'),
	path('collapse/', views.collapse, name='blog-collapse'),
	path('article/', views.article, name='blog-article'),
]
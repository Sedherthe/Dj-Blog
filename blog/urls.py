from django.urls import path
from .views import (PostListView,
 PostDetailView,
 PostCreateView,
 PostUpdateView,
 PostDeleteView,
)
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
	path('post/new', PostCreateView.as_view(), name='blog-create'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
	path('about/', views.about, name='blog-about'),
	path('ddown/', views.ddown, name='blog-ddown'),
	path('nav/', views.nav, name='blog-nav'),
	path('navbar/', views.navbar, name='blog-navbar'),
	path('collapse/', views.collapse, name='blog-collapse'),
	path('article/', views.article, name='blog-article'),
	path('form/', views.form, name='blog-form')
]
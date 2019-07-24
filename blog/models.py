from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Create the Post model

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_published = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	# This function provides path to any specific instance.
	def get_absolute_url(self):
			# redirect will take us to that url
			# reverse will only return the path as a string
			return reverse('blog-detail', kwargs={'pk':self.pk})
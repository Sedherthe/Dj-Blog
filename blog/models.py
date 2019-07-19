from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Create the Post model

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_published = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

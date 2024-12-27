from taggit.managers import TaggableManager
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField('Post', related_name='tags', blank=True)

    def __str__(self):
        return self.name
# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # be sure that you don't put parenthesis after now() though it's a function.
    # because we dont actually execute that function at that point
    # we just want to pass in that function as default value.
    date_posted = models.DateTimeField(default=timezone.now)
    # user:posts = 1:N relationship. only delete posts if post(s) is(Are) deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

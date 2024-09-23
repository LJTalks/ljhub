from django.db import models
from django.contrib.auth.models import User

# Post Status Choices
POST_STATUS_CHOICES = [
    (0, "Draft"),
    (1, "Published")
]

# Comment status choices
COMMENT_STATUS_CHOICES = [
    (0, 'Pending'),
    (1, 'Approved')
]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# Adding Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=COMMENT_STATUS_CHOICES, default=0)
    

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

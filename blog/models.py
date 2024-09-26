from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS_CHOICES, default=0)
    updated_on= models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# Adding Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=COMMENT_STATUS_CHOICES, default=0)
    

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

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
    publish_date = models.DateTimeField(default=timezone.now) # New field for publish date
    excerpt = models.TextField(blank=True)
    views = models.IntegerField(default=0) # New field for tracking views

    class Meta:
        ordering = ['-publish_date']
        
    def __str__(self):
        return f"{self.title} | {self.author}"


# Adding Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # Renamed author for comments, to commenter to avoid confusion with post author
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField() # Renamed content to comment for clarity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=COMMENT_STATUS_CHOICES, default=0)

    @property
    def comment_excerpt(self):
        return self.comment[:50] + '...' if len(self.comment) > 50 else self.comment    

    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.post.title}' # Updated to reflect 'commenter'

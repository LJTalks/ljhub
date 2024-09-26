from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm


# View for listing all blog posts
def blog_list(request):
    # Fetch all published blog posts and order them by creation date, newest first
    posts = Post.objects.filter(status=1).order_by(
        '-created_on')  # Only show published posts
    # Pass the posts to the template
    return render(request, 'blog/blog_list.html', {'posts': posts})


# View for displaying a single blog post and its comments
def blog_post(request, slug):
    queryset = Post.objects.filter(status=1) # Filter to show only published posts
    post = get_object_or_404(queryset, slug=slug)   # Fetch a single post by slug
    comments = post.comments.filter(status=1).count()  # Fetch and count comments for the post
    
    # Initialize 'comment' variable (to avoid the return comment:comment error )
    comment = None

    # Check if comment form is submitted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        'blog/blog_post.html',
        {
            'post': post,
            'comments': comments,
            'comment': comment,
            'comment_form': comment_form
    })

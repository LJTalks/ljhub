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
    comments = post.comments.filter(papproved=True).count()  # Fetch and count comments for the post

    # Check if comment form is submitted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        'blog/blog_post.html',
        {'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })

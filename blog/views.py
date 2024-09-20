from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm


# View for listing all blog posts


def blog_list(request):
    posts = Post.objects.filter(status=1).order_by(
        '-created_on')  # Only show published posts
    return render(request, 'blog/blog-list.html', {'posts': posts})

# View for displaying a single blog post and its comments


def blog_post(request, slug):
    return HttpResponse("Blog post view is working!")

    # post = get_object_or_404(Post, slug=slug)
    # comments = post.comments.filter(post=post)  # Fetch comments for the post
    # new_comment = None

    # # Check if comment form is submitted
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.user = request.user
    #         new_comment.post = post
    #         new_comment.save()
    #     else:
    #         comment_form = CommentForm()

    #     return render(request, 'blog/blog-post.html', {
    #         'post': post,
    #         'comments': comments,
    #         'new_comment': new_comment,
    #         'comment_form': comment_form
    #     })

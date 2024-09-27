from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages # to update users on their comments and log in status
from django.views import generic # to use CBV's
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm # we will use crispy forms

#reverse is for generating URLs , similar to in templates {% url 'view' arg1 arg2 %}

# Function based View for listing all blog posts
def blog_list(request):
    # Fetch all published blog posts and order them by creation date, newest first
    posts = Post.objects.filter(status=1).order_by(
        '-created_on')  # Only show published posts
    # Pass the posts to the template
    return render(request, 'blog/blog_list.html', {'posts': posts})

# Class based views for listing all  the blog posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6
    
    

# View for displaying a single blog post and its comments
def blog_post(request, slug):
    queryset = Post.objects.filter(status=1) # Filter to show only published posts TO ALL
    post = get_object_or_404(queryset, slug=slug)   # Fetch a single post by slug
    comments = post.comments.filter(status=1)  # Fetch approved comments for the post (add count  .count()) 
    
    # Initialize 'comment' variable (to avoid the return comment:comment error )
    # comment = None # do we need this now?

    # Check if comment form is submitted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to the db yet
            comment = comment_form.save(commit=False)
            comment.commenter = request.user # auto assign the logged in user
            comment.post = post # The blog post the new comment refers to 
            comment.save()
            # Send a sucess message to the user if their comment is valid
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return redirect(reverse('blog_post', slug=post.slug)) # Return to the blog post
        
    else:
        comment_form = CommentForm() # if the comment is not valid we should send message? 
        # then return back to the comment form?

    return render(
        request,
        'blog/blog_post.html',
        {
            'post': post,
            'comments': comments,
            # 'comment': comment, # should this be ommitted now? Chat gpt said safe to delete this...
            'comment_form': comment_form
    })

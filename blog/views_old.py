from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages # to update users on their comments and log in status
from django.views import generic # to use CBV's
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm # we use crispy forms


# Class based view for listing all the blog posts # (used in walkthrough)
class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog_list.html"
    context_object_name = 'posts' #ensures consistency in template context naming
    paginate_by = 6
    

# View for displaying a single blog post and its comments
def blog_post(request, slug):
    queryset = Post.objects.filter(status=1) # Filter to show only published posts TO ALL
    post = get_object_or_404(queryset, slug=slug)   # Fetch a single post by slug
    post.views += 1
    post.save()
    
    comments = post.comments.all().order_by("created_at")
    comment_count = post.comments.filter(status=1).count()  # Fetch approved comments for the post and add count 
    
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
        
    else:
        comment_form = CommentForm() #
        # then return back to the comment form?

    return render(
        request,
        'blog/blog_post.html',
        {
            'post': post,
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form,
    },
    )

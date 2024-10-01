from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic  # to use CBV's
from django.contrib import messages  # update users on comments/log in status
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm  # we use crispy forms


# Class based view for listing all the blog posts
class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog_list.html"
    context_object_name = 'posts'  # consistent template context naming
    paginate_by = 6


# View for displaying a single blog post and its comments
def blog_post(request, slug):
    """
    Display an individual :model :'blog_post'.
    **Context**
    ``post``
    An instance of :model:`blog.Post`.
    
    **Template**
    ;template:`blog/blog_list.html`
    """
    # print("Inside blog_post view")  # Debug. Is the view called
    queryset = Post.objects.filter(status=1)  # Filter published posts
    post = get_object_or_404(queryset, slug=slug)   # Fetch single post by slug
    post.views += 1
    post.save()

    comments = post.comments.all().order_by("created_at")
    # approved comments for the post and add count
    comment_count = post.comments.filter(status=1).count()

    if request.method == 'POST':
        print("received a POST request")  # Debugging
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create a comment object but don't save to the db yet
            comment = comment_form.save(commit=False)
            comment.commenter = request.user  # auto assign the logged in user
            comment.post = post  # The blog post the new comment refers to
            comment.save()

            # Send a sucess message to the user if their comment is valid
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            
            # Redirect to the blog post page to avoid form resubmission
            return HttpResponseRedirect(reverse('blog_post', args=[slug]))
            # if the comment is not valid we should send message?
            # then return back to the comment form?
    else:
        # Handles GET requests and invalid forms
        comment_form = CommentForm()
        
    print("about to render template") # Debugging
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


# View to edit comments
def comment_edit(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post  # already linked to the post or treating the
            # updated comment as new comment so need to link it to the post
            comment_approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating!")

    return HttpResponseRedirect(reverse("blog_post", args=[slug]))


# View to delete comments
def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    # do we need to get the post again just to delete the comment?
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("blog_post", args=[slug]))
    
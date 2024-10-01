from . import views
from django.urls import path


urlpatterns = [
    # this is the blog home page that has all the blogs
    path("", views.BlogList.as_view(), name="blog_list"), # The blog home page/list view
    path('<slug:slug>/', views.blog_post, name='blog_post'), # Individual Blog posts with slug address 
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit',
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete,
        name="comment_delete",
    ),
]

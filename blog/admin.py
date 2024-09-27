from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register your models here.

# Admin panel for managing blog posts 
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # fields to dispaly in the admin panel for the Post model 
    list_display = ('title', 'slug', 'status', 'created_on')
    # Enable search functionality in these fields
    search_fields = ['title', 'content']
    # filters narrow down displayed posts
    list_filter = ('status', 'created_on')
    # Automate the slug population
    prepopulated_fields = {'slug': ('title',)}
    # WYSIWYG fields
    summernote_fields = ('content',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # commenter and post title/author should be auto filled?
    list_display = ('post', 'commenter', 'status', 'created_at', 'updated_at')
    search_fields = ['commenter__username', 'comment'] # Changed from 'content' to reflect model changes
    list_filter = ('post', 'created_at', 'status')
    actions = ['approve_comments', 'delete_comments'] # Approve and delete from admin list view
    
    # Display human readable comment status in admin 
    def get_status(self, obj):
        return obj.get_status_display()
    # custom header for get-status column
    get_status.short_description = 'Status'
    
    # Action to approve multiple comments
    def approve_comments(self, request, queryset):
        queryset.update(status=1)
    # Custom label for the approve_comments action in the admin panel
    approve_comments.short_description = "Approve selected comments"
    
    # Over ride save model to auto fill commenter field in admin panel 
    # the logged in user is the commenter
    # the following code suggested by chatgpt
def save_model(self, request, obj, form, change):
        # If the commenter field is not set, use the current logged-in admin user as the commenter
        # Last comment is a bit weird; why would it not be set 🤣
       if not obj.commenter:
           obj.commenter = request.user
           # Save the object to the database
           super().save_model(request, obj, form, change)
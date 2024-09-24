from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment



# Register your models here.
# Admin panel 
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'post', 'created_at', 'get_status')
    search_fields = ['content']
    list_filter = ('post', 'created_at', 'status')
    actions = ['approve_comments', 'delete_comments']
    
    def get_status(self, obj):
        return obj.get_status_display()
    get_status.short_description = 'Status'
    
    # Action to approve comments
    def approve_comments(self, request, queryset):
        queryset.update(status=1)
    approve_comments.short_description = "Approve selected comments"
    
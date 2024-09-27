from django import forms
from .models import Comment

# the form users will create comments in. 
# The post and author should be auto filled, along with the commenters name
# the only field presented to user will be the comment field
# check if the admin panel needs these changes 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] # only show the comment field to the user # adjusted from content to reflect change in model

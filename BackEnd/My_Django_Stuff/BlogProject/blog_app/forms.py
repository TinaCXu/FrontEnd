from django import forms
from blog_app import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('author','title','text')
        widgets={'author':forms.TextInput(attrs={'class':'textinputclass'}),
                    'title':forms.TextInput(attrs={'class':'textinputclass'}),
                    'text':forms.TextInput(attrs={'class':'textinputclass'})}
        # this textinputclass should be in html & css
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ('author','text')
        widgets={'author':forms.TextInput(attrs={'class':'textinputclass'}),
                    'text':forms.TextInput(attrs={'class':'textinputclass'})}
  

            
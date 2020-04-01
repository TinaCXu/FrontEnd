from django.shortcuts import render
from django.utils import timezone
from . import models
from django.views.generic import TemplateView,ListView

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
class Cre

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.object.filter(published_date__lte=timezone.now()).order_by('published_date')
        # __lte means <=
class PostDetailView()
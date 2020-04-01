from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # different arguement with teacher
    create_date = models.DateTimeField() 
    published_date = models.DateTimeField(null=True,blank=True,auto_now=True)
    # auto_now=True: The field is only automatically updated when calling Model.save().
    def publish(self):
        published_date = timezone.now()
        self.save()    
    def approve_comments(self):
        return self.Comments.filter(approve_comments=True)
        ## problem with member Comments
    def absolute_url(self):
        reverse('post_list')
        ## url name: post_list
    def __str__(self):
        return self.title
class Comments(models.Model):
    post = models.ForeignKey('blog_app.models.Post',on_delete=models.CASCADE)
    author = models.CharField()
    text = models.TextField()
    create_date = models.DateTimeField()
    approve_comments = models.BooleanField(default=False)
    # BooleanField: true or false field
    def approve(self):
        approve_comments = True
        self.save()
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
        ## whose PK??
    def __str__(self):
        return self.text
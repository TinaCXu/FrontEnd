from django.conf.urls import url
from . import views

urlpatterns = [
    url('about/',views.AboutView.as_view(), name='about'),
    url('post/pk')
]
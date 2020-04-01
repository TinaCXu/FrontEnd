from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url('',views.SchoolListView.as_view(),name='list'),    
    url('<int:school_pk>/',views.SchoolDetailView.as_view(),name='detail'),
]
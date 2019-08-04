from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.blog_home_page, name='blog_home_page'),
    path('page', views.get_blog_page, name='get_blog_page'),
]

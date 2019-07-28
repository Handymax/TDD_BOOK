from django.conf.urls import url
from blogs import views

urlpatterns = [
    url(r'^$', views.blog_home_page, name='blog_home_page'),
    url(r'^page$', views.get_blog_page, name='get_blog_page'),
]

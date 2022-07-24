from django.urls import path
from . import views

urlpatterns = [
    # load starting page with lists of latest blog posts and some welcome text
    path('', views.index, name='index-page'),  # / path
    # load page which lists all blog posts
    path('posts', views.posts, name='posts-page'),  # /posts
    # load individual blog post page which shows full blog post
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page')  # /posts/my-blog-post
]

from django.urls import path
from . import views

urlpatterns = [
    # load starting page with lists of latest blog posts and some welcome text
    # path('', views.index, name='index-page'),  # / path
    path("", views.IndexPageView.as_view(), name="index-page"),
    # load page which lists all blog posts
    # path('all-posts', views.posts, name='posts-page'),  # /posts
    path("all-posts", views.AllPostsView.as_view(), name="posts-page"),
    # load individual blog post page which shows full blog post
    # path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),  # /posts/my-blog-post
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]

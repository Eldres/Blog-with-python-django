from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class IndexPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date", ]
    # setting this field to match the previous func `posts` being sent to the context so our template views don't need to be updated
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]  # orders in DESC order using the `-`
#     return render(request, 'blog/index.html', {
#         "posts": latest_posts
#     })

class AllPostsView(ListView):
    template_name: str = "blog/all-posts.html"
    model = Post
    ordering = ["-date", ]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })


class SinglePostView(DetailView):
    template_name: str = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        return context


# def post_detail(request, slug):
#     found_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": found_post,
#         "post_tags": found_post.tag.all()
#     })

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm


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


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later - False
        return is_saved_for_later

    def create_context(self, request, post_data):
        return {
            "post": post_data,
            "post_tags": post_data.tag.all(),
            "comment_form": CommentForm(),
            "comments": post_data.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post_data.id)
        }

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = self.create_context(request, post)
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = self.create_context(request, post)
        return render(request, "blog/post-detail.html", context)


# def post_detail(request, slug):
#     found_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": found_post,
#         "post_tags": found_post.tag.all()
#     })

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

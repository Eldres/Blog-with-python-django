from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Josh",
        "date": date(2022, 6, 3),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! Sometimes, you're never prepared for what happens whilst enjoying the views!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur quibusdam, 
          obcaecati harum sapiente iure nulla eligendi ipsa cupiditate? Molestias a
          blanditiis aliquid est, neque inventore veritatis odio provident iste 
          similique?

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur quibusdam,
          obcaecati harum sapiente iure nulla eligendi ipsa cupiditate? Molestias a
          blanditiis aliquid est, neque inventore veritatis odio provident iste
          similique?

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur quibusdam,
          obcaecati harum sapiente iure nulla eligendi ipsa cupiditate? Molestias a
          blanditiis aliquid est, neque inventore veritatis odio provident iste
          similique?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Josh",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Josh",
        "date": date(2020, 8, 5),
        "title": "Nature At It's Best!",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post.get('date')


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    found_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
      "post": found_post
    })

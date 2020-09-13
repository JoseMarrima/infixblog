from django.shortcuts import render
from django.views import generic
from blog.models import Post, Comment



# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, "blog_category.html", context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_details.html'

def index(request):
    return render(request,'blog/index.html',)

def contact(request):
    return render(request,'blog/contact.html',)
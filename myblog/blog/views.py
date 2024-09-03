from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch a single post by primary key (pk)
    return render(request, 'blog/post_detail.html', {'post': post})

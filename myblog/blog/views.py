from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post


def landing_page(request):
    posts_list = Post.objects.all()  # Fetch all posts from the database
    paginator = Paginator(posts_list, 4)  # Paginate with 4 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/landing_page.html', {
        'posts': posts,
        'paginator': paginator
    })


def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch a single post by primary key (pk)
    return render(request, 'blog/post_detail.html', {'post': post})

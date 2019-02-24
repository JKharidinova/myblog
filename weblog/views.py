from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'weblog/home.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'weblog/detail.html', {'post': post})


def post_edit(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else Post()
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = form.save()
            post.pub_date = timezone.now()
            post.save()
            return redirect('weblog:detail', pk=post.pk)

    return render(request, 'weblog/post_edit.html', {'form': form})

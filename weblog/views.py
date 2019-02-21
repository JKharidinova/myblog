from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone

from .models import Blogs
from .forms import PostForm


class BlogsView(generic.ListView):
    template_name = 'weblog/index.html'
    context_object_name = 'title_list'

    def get_queryset(self):
        return Blogs.objects.all()


class PostsView(generic.DetailView):
    model = Blogs
    template_name = 'weblog/detail.html'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

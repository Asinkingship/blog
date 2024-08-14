from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)
from .models import Post
# from django.urls import reverse


class PostListView(ListView):                           # scan
    template_name = 'posts/list.html'
    model = Post

class PostDetailView(DetailView):                       # read single
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(CreateView):                       # create new records
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body']

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    success_url = reverse_lazy("list")
    # success_url = reverse("list")
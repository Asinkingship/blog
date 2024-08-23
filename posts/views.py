from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Post, Status
# from django.urls import reverse


class PostListView(ListView):                           # scan
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub_status = Status.objects.get(name="published")
        context["post_list"] = (
            Post.objects
            .filter(status=pub_status)
            .order_by("created_on").reverse()
        )
        return context
    
class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = (
            Post.objects
            .filter(status=draft_status)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context
    
class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        arch_status = Status.objects.get(name="archives")
        context["post_list"] = (
            Post.objects
            .filter(status=arch_status)
            .order_by("created_on").reverse()
        )
        return context

class PostDetailView(DetailView):                       # read single
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):                       # create new records
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
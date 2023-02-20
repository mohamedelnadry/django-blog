from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "pages/home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "pages/detail_view.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "pages/post_create.html"
    fields = ['title','author','body']
class BlogUpdatteView(UpdateView):
    model = Post
    template_name = "pages/post_edit.html"
    fields = ['title','body']
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = reverse_lazy("home")

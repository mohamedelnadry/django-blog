from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdatteView, BlogDeleteView


urlpatterns = [
    path("",BlogListView.as_view(),name="home"),
    path("post/<int:pk>/",BlogDetailView.as_view(),name="post_detail"),
    path("post/add/",BlogCreateView.as_view(),name="post_add"),
    path("post/<int:pk>/edit/",BlogUpdatteView.as_view(),name="post_edit"),
    path("post/<int:pk>/delete/",BlogDeleteView.as_view(),name="post_delete"),

]

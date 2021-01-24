from datetime import datetime, timezone
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from estore.services import get_all_object_list, get_object_cache
from .models import PostCategory, PostComment, PostImage, Post, PostTag

def get_day_diff(post_date):
    now = datetime.now(timezone.utc)
    diff = now - post_date
    return diff.days

def get_extra_ctx_data(context):
    context['category_list'] = PostCategory.objects.all()
    context['tags_list'] = PostTag.objects.all()
    context['recent_posts'] = []
    for post in Post.objects.all():
        diff = get_day_diff(post.date)
        context['recent_posts'].append(post) if diff < 15 else None
    return context


class PostDetailView(DetailView):
    template_name = 'single-blog.html'
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        return get_extra_ctx_data(context)


class PostListView(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'post_list'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        return get_extra_ctx_data(context)

class PostCategoryListView(ListView):
    template_name = "post_category_list.html"
    model = PostCategory

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        return get_extra_ctx_data(context)

class PostCategoryDetailView(DetailView):
    template_name = 'post_category_detail.html'
    model = PostCategory
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        return get_extra_ctx_data(context)
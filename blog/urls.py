from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCategoryListView, PostCategoryDetailView,)
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post-detail"),
    path('category/', PostCategoryListView.as_view(), name="post-category-list"),
    path('category/<slug:slug>/', PostCategoryDetailView.as_view(), name="post-category-detail"),
]
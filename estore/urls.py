from django.urls import path
from .views import (HomeView, ProductCategoryListView,
                    ProductCategoryDetailView,
                    ProductListView, ProductDetailView,
                    ProductCollectionListView, ProductCollectionDetailView,
                    )

app_name = 'estore'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/', ProductCategoryListView.as_view(), name='category'),
    path('category/<slug:slug>/', ProductCategoryDetailView.as_view(), name='category-detail'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('collection/', ProductCollectionListView.as_view(), name='collection-list'),
    path('collection/<slug:slug>/', ProductCollectionDetailView.as_view(), name='collection-detail'),

]
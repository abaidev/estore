from django.urls import path
from .views import (ProductListAPIView, ProductRUDView, ProductCreateAPIView,
                    ProductCategoryListAPIView, ProductCategoryRUDView, ProductCategoryCreateAPIView,
                    ProductCollectionListAPIView, ProductCollectionRUDView, ProductCollectionCreateAPIView, )

app_name = 'estore-api'

urlpatterns = [
    # PRODUCTS
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRUDView.as_view(), name='product-rud'),

    # PRODUCTS CATEGORY
    path('prod_cat/', ProductCategoryListAPIView.as_view(), name='product-cat'),
    path('prod_cat/create/', ProductCategoryCreateAPIView.as_view(), name='product-cat-create'),
    path('prod_cat/<slug:slug>/', ProductCategoryRUDView.as_view(), name='product-cat-rud'),

    # PRODUCTS COLLECTIONS
    path('prod_coll/', ProductCollectionListAPIView.as_view(), name='product-coll'),
    path('prod_coll/create/', ProductCollectionCreateAPIView.as_view(), name='product-coll-create'),
    path('prod_coll/<slug:slug>/', ProductCollectionRUDView.as_view(), name='product-coll-rud'),
]
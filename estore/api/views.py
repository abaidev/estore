from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from estore.models import Product, ProductImage, ProductCategory, ProductCollection
from .serializers import (ProductListSerializer, ProductRUDSerializer, ProductSerializer,
                          ProductCategorySerializer, ProductCollectionSerializer, ProductCollectionListSerializer)
from .permissions import IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly
from .paginations import EstoreLimitOffsetPagination


# PRODUCT
class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class = EstoreLimitOffsetPagination

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductRUDSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]


# PRODUCT CATEGORY
class ProductCategoryListAPIView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    pagination_class = EstoreLimitOffsetPagination

class ProductCategoryRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]

class ProductCategoryCreateAPIView(CreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]


# PRODUCT COLLECTIONS
class ProductCollectionListAPIView(ListAPIView):
    serializer_class = ProductCollectionListSerializer
    queryset = ProductCollection.objects.all()
    pagination_class = EstoreLimitOffsetPagination

class ProductCollectionRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCollectionSerializer
    queryset = ProductCollection.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]

class ProductCollectionCreateAPIView(CreateAPIView):
    serializer_class = ProductCollectionSerializer
    queryset = ProductCollection.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, MyIsAdminOrReadOnly]
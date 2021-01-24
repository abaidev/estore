from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import ProductCategory, Product, ProductCollection
from .services import CACHE_TTL, get_all_object_list, get_object_cache

# HOME VIEW (INDEX)
@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {
            'collections': get_all_object_list(ProductCollection),
            'category_list': get_all_object_list(ProductCategory),
            'all_products': get_all_object_list(Product),
        })

# PRODUCT CATEGORY
@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductCategoryListView(ListView):
    template_name = 'category.html'
    model = ProductCategory
    context_object_name = 'category_list'
    queryset = get_all_object_list(model)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_products'] = get_all_object_list(Product)
        return context

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductCategoryDetailView(DetailView):
    template_name = 'category.html'
    model = ProductCategory
    queryset = model.objects.all()

    def get_queryset(self):
        return get_object_cache(self.queryset, 'slug', self.kwargs['slug'])


# PRODUCT
@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'all_products'
    queryset = get_all_object_list(model)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = get_all_object_list(ProductCategory)
        return context

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product.html'
    queryset = get_all_object_list(model)

    def get_queryset(self):
        return get_object_cache(self.queryset, 'pk', self.kwargs['pk'])

@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductCollectionListView(ListView):
    model = ProductCollection
    template_name = 'collection_list.html'
    context_object_name = 'collections'
    queryset = get_all_object_list(model)


# PRODUCT COLLECTION
@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductCollectionDetailView(DetailView):
    model = ProductCollection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'
    queryset = get_all_object_list(model)

    def get_queryset(self):
        return get_object_cache(self.queryset, "slug", self.kwargs['slug'])

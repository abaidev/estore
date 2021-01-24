from rest_framework import serializers
from estore.models import ProductCollection, Product, ProductCategory, ProductImage

# PRODUCT
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['price_final']


class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='pk', view_name='estore-api:product-rud')
    discount = serializers.SerializerMethodField()
    gtype = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    def get_discount(self, obj):
        return f"{obj.discount} %"

    def get_gtype(self, obj):
        return obj.get_gtype_display()

    def get_category(self, obj):
        return obj.category.slug


class ProductRUDSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [field.name for field in model._meta.fields] + ['pictures']
        depth = 2

    def get_pictures(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(pict.image.url) for pict in obj.productimage_set.all()]


# PRODUCT IMAGE
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


# PRODUCT CATEGORY
class ProductCategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='estore-api:product-cat-rud', lookup_field='slug')
    class Meta:
        model = ProductCategory
        fields = '__all__'
        extra_kwargs = {"cover": {"required": False}, "slug": {"read_only": True}}


# PRODUCT COLLECTIONS
class ProductCollectionListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='estore-api:product-coll-rud', lookup_field='slug')
    class Meta:
        model = ProductCollection
        fields = '__all__'

class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = '__all__'
        extra_kwargs = {"slug": {"read_only": True}, "banner": {"required": False}}

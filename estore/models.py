from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class ProductCategory(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='product-cats') #, default='product-cats/default-prod.png'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    GENDERS_TYPES = (
        ('m', 'men'),
        ('w', 'women')
    )
    gtype = models.CharField(max_length=2, choices=GENDERS_TYPES)
    name = models.CharField(max_length=500, db_index=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price_initial = models.FloatField(default=0, validators=[MinValueValidator(0)])
    discount = models.FloatField(default=0, verbose_name='Discount in (%)', validators=[MinValueValidator(0), MaxValueValidator(100)])
    price_final = models.FloatField(default=0, validators=[MinValueValidator(0)])
    amount = models.IntegerField(default=0)
    description = RichTextField(null=True, blank=True)
    rating = models.IntegerField(verbose_name="Product Rating", validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_recieved = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.discount = round(self.discount, 2)
        self.price_final = round(self.price_initial - (self.discount * self.price_initial / 100), 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ${self.price_final}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products') #, default='products/default-prod.png'
    main_img = models.BooleanField(verbose_name="Is Main Picture", default=False)

    def __str__(self):
        return self.product.name + ".img"


class ProductCollection(models.Model):
    name = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField()
    collection = models.ManyToManyField(Product, blank=True, default=None, related_name='prod_collection')
    date_created = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='collections', null=True, blank=True)
    max_discount = models.IntegerField(default=0)
    summary = models.CharField(max_length=1200)
    best_of_month = models.BooleanField(default=False)
    slider_collection = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " collection"
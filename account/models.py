from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from estore.models import Product

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, verbose_name='First Name')
    last_name = models.CharField(max_length=500, verbose_name='Last Name')
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='profiles') #, default='profiles/default-profile.png'
    wish_list = models.ManyToManyField(Product, verbose_name='Wish List', default=None, blank=True, related_name='wish_list')
    favorites = models.ManyToManyField(Product, verbose_name='Favorites', default=None, blank=True, related_name='favorites')
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('account:profile', kwargs={"username": self.user.username})

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, verbose_name='First Name')
    last_name = models.CharField(max_length=500, verbose_name='Last Name')
    created_date = models.DateTimeField(auto_now_add=True)
    slogan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username



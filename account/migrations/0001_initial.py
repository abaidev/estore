# Generated by Django 3.1.5 on 2021-01-07 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estore', '0004_auto_20210107_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=500, verbose_name='Last Name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('slogan', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=500, verbose_name='Last Name')),
                ('birth_date', models.DateField()),
                ('photo', models.ImageField(upload_to='profiles')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('favorites', models.ManyToManyField(blank=True, default=None, related_name='favorites', to='estore.Product', verbose_name='Favorites')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wish_list', models.ManyToManyField(blank=True, default=None, related_name='wish_list', to='estore.Product', verbose_name='Wish List')),
            ],
        ),
    ]

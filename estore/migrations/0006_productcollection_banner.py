# Generated by Django 3.1.5 on 2021-01-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0005_productcollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcollection',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='collections'),
        ),
    ]

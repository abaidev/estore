# Generated by Django 3.1.5 on 2021-01-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0008_productcollection_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcollection',
            name='best_of_month',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0004_auto_20210107_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('collection', models.ManyToManyField(blank=True, default=None, related_name='prod_collection', to='estore.Product')),
            ],
        ),
    ]

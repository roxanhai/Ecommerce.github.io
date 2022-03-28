# Generated by Django 3.0.1 on 2022-03-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B', 'Book'), ('MP', 'Mobile Phone'), ('C', 'Clothes'), ('L', 'Laptop'), ('S', 'Shoes'), ('E', 'Electronics')], default='B', max_length=20),
        ),
    ]

# Generated by Django 3.0.1 on 2022-03-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20220323_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='61570', max_length=200, null=True, unique=True),
        ),
    ]

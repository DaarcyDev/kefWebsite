# Generated by Django 4.2.3 on 2023-07-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.AddField(
            model_name='product',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_female',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_male',
            field=models.BooleanField(default=False),
        ),
    ]

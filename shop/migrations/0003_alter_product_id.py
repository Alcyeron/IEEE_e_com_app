# Generated by Django 4.2.5 on 2023-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_image_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]

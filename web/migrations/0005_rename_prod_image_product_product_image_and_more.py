# Generated by Django 4.2 on 2023-04-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_product_prod_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_tag',
            new_name='product_tag',
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

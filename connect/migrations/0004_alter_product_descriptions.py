# Generated by Django 4.2 on 2023-05-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_remove_order_products_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothadmin', '0004_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(db_column='price', max_length=50, null=True),
        ),
    ]

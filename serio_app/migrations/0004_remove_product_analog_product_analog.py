# Generated by Django 4.2.2 on 2023-06-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serio_app', '0003_remove_category_glob_cat_product_analog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='analog',
        ),
        migrations.AddField(
            model_name='product',
            name='analog',
            field=models.ManyToManyField(blank=True, null=True, to='serio_app.product', verbose_name='Analog'),
        ),
    ]
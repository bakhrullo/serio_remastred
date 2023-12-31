# Generated by Django 4.2.2 on 2023-06-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serio_app', '0004_remove_product_analog_product_analog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.CharField(default=1, max_length=15, verbose_name='Telefon raqami'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='analog',
            field=models.ManyToManyField(blank=True, to='serio_app.product', verbose_name='Analog'),
        ),
    ]

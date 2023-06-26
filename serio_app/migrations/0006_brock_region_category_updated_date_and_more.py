# Generated by Django 4.2.2 on 2023-06-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serio_app', '0005_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Xizmatlar',
                'verbose_name_plural': 'Xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Viloyatlar',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana"),
        ),
        migrations.AddField(
            model_name='globcat',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana"),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana"),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana"),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana"),
        ),
        migrations.AlterField(
            model_name='globcat',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana"),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana"),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana"),
        ),
    ]

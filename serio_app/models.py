from django.db import models


class GlobCat(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name='kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='kategroiya nomi en')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Bosh kategroiyalar"
        verbose_name_plural = "Bosh kategroiyalar"


class Category(models.Model):
    glob_cat = models.ForeignKey(GlobCat, on_delete=models.CASCADE, verbose_name='Bosh kategoriya')
    name_uz = models.CharField(max_length=200, verbose_name='Kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='Kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Kategroiya nomi en')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kategroiyalar"
        verbose_name_plural = "Kategroiyalar"


class Product(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    name_ru = models.CharField(max_length=200, verbose_name='Tovar nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    price = models.CharField(max_length=100, verbose_name='Tovar narxi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Tovar kategoriyasi')
    descr_uz = models.TextField(verbose_name='Tovar ma\'lumotlari en')
    descr_ru = models.TextField(verbose_name='Tovar ma\'lumotlari ru')
    descr_en = models.TextField(verbose_name='Tovar ma\'lumotlari en')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ism', null=True)
    tg_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Telegram id')
    lang = models.CharField(max_length=2, verbose_name='Tili')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam', null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


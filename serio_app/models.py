from django.db import models


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")

    class Meta:
        abstract = True


class GlobCat(Base):
    name_uz = models.CharField(max_length=200, verbose_name='kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='kategroiya nomi en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Bosh kategroiyalar"
        verbose_name_plural = "Bosh kategroiyalar"


class Category(Base):
    glob_cat = models.ForeignKey(GlobCat, on_delete=models.CASCADE, verbose_name='Bosh kategoriya')
    name_uz = models.CharField(max_length=200, verbose_name='Kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='Kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Kategroiya nomi en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kategroiyalar"
        verbose_name_plural = "Kategroiyalar"


class Product(Base):
    name_uz = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    name_ru = models.CharField(max_length=200, verbose_name='Tovar nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    price = models.CharField(max_length=100, verbose_name='Tovar narxi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Tovar kategoriyasi')
    descr_uz = models.TextField(verbose_name='Tovar ma\'lumotlari en')
    descr_ru = models.TextField(verbose_name='Tovar ma\'lumotlari ru')
    descr_en = models.TextField(verbose_name='Tovar ma\'lumotlari en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class User(Base):
    name = models.CharField(max_length=200, verbose_name='Ism', null=True)
    tg_id = models.PositiveBigIntegerField(unique=True, verbose_name='Telegram id')
    lang = models.CharField(max_length=2, verbose_name='Tili')
    role = models.CharField(max_length=100, verbose_name='Soha', null=True)
    phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam', null=True)

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


class Brock(Base):
    name_uz = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    name_ru = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Nomi', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xizmat turlari"
        verbose_name_plural = "Xizmat turlari"


class Region(Base):
    name_uz = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    name_ru = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Nomi', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Viloyatlar"
        verbose_name_plural = "Viloyatlar"

class Service(Base):
    name = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    phone = models.CharField(max_length=100, verbose_name='Raqam')
    weight = models.CharField(max_length=100, verbose_name='Og\'irligi')
    region = models.ManyToManyField(Region, verbose_name='Viloyat')
    brock = models.ManyToManyField(Brock, verbose_name='Xizmat')
    def __str__(self):
        return self.name

    def brock_see(self):
        return ",\n".join([g.name for g in self.brock.all()])
    def region_see(self):
        return ",\n".join([g.name for g in self.region.all()])
    class Meta:
        verbose_name = "Xizmatchilar"
        verbose_name_plural = "Xizmatchilar"

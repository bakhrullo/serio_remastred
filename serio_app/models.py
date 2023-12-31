from django.db import models


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")

    class Meta:
        abstract = True


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
    name_uz = models.CharField(max_length=100, verbose_name='Nomi uz', unique=True)
    name_ru = models.CharField(max_length=100, verbose_name='Nomi ru', unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Nomi en', unique=True)
    image = models.ImageField(default="media/no-photo_5TKbPdH.png")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Xizmat turlari"
        verbose_name_plural = "Xizmat turlari"


class Region(Base):
    name_uz = models.CharField(max_length=100, verbose_name='Nomi uz', unique=True)
    name_ru = models.CharField(max_length=100, verbose_name='Nomi ru', unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Nomi en', unique=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Viloyatlar"
        verbose_name_plural = "Viloyatlar"


class Service(Base):
    name = models.CharField(max_length=100, verbose_name='Nomi', unique=True)
    phone = models.CharField(max_length=100, verbose_name='Raqam')
    weight = models.CharField(max_length=100, verbose_name='Og\'irligi', null=True, blank=True)
    region = models.ManyToManyField(Region, verbose_name='Viloyat')
    brock = models.ManyToManyField(Brock, verbose_name='Xizmat')

    def __str__(self):
        return self.name

    def Xizmatlar(self):
        return ",\n".join([g.name_uz for g in self.brock.all()])

    def Viloyatlar(self):
        return ",\n".join([g.name_uz for g in self.region.all()])

    class Meta:
        verbose_name = "Xizmatchilar"
        verbose_name_plural = "Xizmatchilar"


class GlobCategory(Base):
    name_uz = models.CharField(max_length=200, verbose_name='Kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='Kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Kategroiya nomi en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Bosh Kategroiyalar"
        verbose_name_plural = "Bosh Kategroiyalar"


class Category(Base):
    glob_cat = models.ForeignKey(GlobCategory, on_delete=models.CASCADE, null=True, verbose_name='Bosh kategoriya')
    name_uz = models.CharField(max_length=200, verbose_name='Kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='Kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Kategroiya nomi en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kategroiyalar"
        verbose_name_plural = "Kategroiyalar"


class SubCategory(Base):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    name_uz = models.CharField(max_length=200, verbose_name='Kategroiya nomi uz')
    name_ru = models.CharField(max_length=200, verbose_name='Kategroiya nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Kategroiya nomi en')

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kichik Kategroiyalar"
        verbose_name_plural = "Kichik Kategroiyalar"


class Product(Base):
    name_uz = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    name_ru = models.CharField(max_length=200, verbose_name='Tovar nomi ru')
    name_en = models.CharField(max_length=200, verbose_name='Tovar nomi en')
    phone = models.CharField(verbose_name='Telefon raqami', max_length=15)
    region = models.ForeignKey(Region, verbose_name='Tovar hududi', on_delete=models.CASCADE)
    made_in = models.CharField(max_length=100, null=True, verbose_name='Tovar ishlab chiqarligan shahar')
    analog = models.ManyToManyField("self", blank=True, verbose_name='Analog')
    price = models.CharField(max_length=100, verbose_name='Tovar narxi')
    sub_category = models.ForeignKey(SubCategory, null=True, on_delete=models.CASCADE, verbose_name='Tovar kategoriyasi')
    descr_uz = models.TextField(verbose_name='Tovar ma\'lumotlari en', null=True, blank=True)
    descr_ru = models.TextField(verbose_name='Tovar ma\'lumotlari ru', null=True, blank=True)
    descr_en = models.TextField(verbose_name='Tovar ma\'lumotlari en', null=True, blank=True)

    def __str__(self):
        return self.name_uz

    def Analoglar(self):
        return ",\n".join([g.name_uz for g in self.analog.all()])

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class Images(Base):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="media/no-photo_5TKbPdH.png")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rasimlar"
        verbose_name_plural = "Rasimalar"
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tg_id', 'phone', 'lang', 'created_date']
    list_filter = ['name', 'tg_id', 'phone', 'created_date']
    search_fields = ['name',  'tg_id', 'phone']


class GlobCatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'created_date']
    list_filter = ['name_uz', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en']
    search_fields = ['name_uz']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'created_date']
    list_filter = ['name_uz', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en']
    search_fields = ['name_uz']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'category', 'created_date']
    list_filter = ['name_uz', 'category']
    list_editable = ['name_uz', 'name_ru', 'name_en', 'category']
    search_fields = ['name_uz']


admin.site.unregister(Group)
admin.site.register(GlobCat, GlobCatAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'

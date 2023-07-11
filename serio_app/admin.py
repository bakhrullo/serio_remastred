from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tg_id', 'phone', 'role', 'lang', 'created_date']
    list_filter = ['name', 'tg_id', 'phone', 'created_date']
    search_fields = ['name', 'tg_id', 'phone']


class GlobCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'created_date']
    list_filter = ['name_uz', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en']
    search_fields = ['name_uz']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'glob_cat', 'created_date']
    list_filter = ['name_uz', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en', 'glob_cat']
    search_fields = ['name_uz']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'cat', 'created_date']
    list_filter = ['name_uz', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en', 'cat']
    search_fields = ['name_uz']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'made_in', 'sub_category', 'Analoglar', 'created_date']
    list_filter = ['name_uz', 'sub_category']
    list_editable = ['name_uz', 'name_ru', 'name_en', 'sub_category', 'made_in']
    search_fields = ['name_uz']


class UnAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru', 'name_en', 'created_date']
    list_editable = ['name_uz', 'name_ru', 'name_en']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'weight', 'Viloyatlar', 'Xizmatlar', 'created_date']
    list_editable = ['name', 'phone', 'weight']
    search_fields = ['name', 'phone', 'weight']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_editable = ['image']
    fields = ['name', 'image']
    readonly_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.unregister(Group)
admin.site.register(Region, UnAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Brock, UnAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(GlobCategory, GlobCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'

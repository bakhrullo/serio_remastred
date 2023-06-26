from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BrockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brock
        fields = '__all__'


class GlobCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobCat
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    glob_cat = GlobCatSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

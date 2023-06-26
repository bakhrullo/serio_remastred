from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from .serializers import *


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class UserGetView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()

class BrockListView(ListAPIView):
    serializer_class = BrockSerializer
    queryset = User.objects.all()


class GlobCatGetView(RetrieveAPIView):
    serializer_class = GlobCatSerializer
    queryset = GlobCat.objects.all()
    lookup_field = "id"


class GlobCatListView(ListAPIView):
    serializer_class = GlobCatSerializer
    queryset = GlobCat.objects.all()


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        option = self.request.query_params.get("option")
        return Category.objects.filter(glob_cat_id=option)


class ProductSearchView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        lang, option = self.request.query_params.get('lang'),  self.request.query_params.get('option')
        if lang == "uz":
            return Category.objects.filter(name_uz__icontains=option)
        elif lang == "ru":
            return Category.objects.filter(name_ru__icontains=option)
        else:
            return Category.objects.filter(name_en__icontains=option)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        prod_cat_id = self.request.query_params.get('cat_id')
        return Product.objects.filter(category_id=prod_cat_id)


class ProductGetView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"

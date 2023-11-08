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
    queryset = Brock.objects.all()


class RegionListView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class ServiceListView(ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(brock=self.request.query_params.get("brock"),
                                      region=self.request.query_params.get("region"))


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        option = self.request.query_params.get("option")
        cat_id = self.request.query_params.get("cat_id")
        if option == "glob":
            return GlobCategory.objects.all()
        elif option == "cat":
            return Category.objects.filter(glob_cat_id=cat_id)
        elif option == "sub":
            return SubCategory.objects.filter(cat_id=cat_id)


class AnalogListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(analog=self.request.query_params.get("prod_id"))


class AnalogTypeListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(name=self.request.query_params.get("name"))


class ProductSearchView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        lang, option = self.request.query_params.get('lang'), self.request.query_params.get('option')
        if lang == "uz":
            return Product.objects.filter(name_uz__icontains=option)
        elif lang == "ru":
            return Product.objects.filter(name_ru__icontains=option)
        else:
            return Product.objects.filter(name_en__icontains=option)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        prod_cat_id = self.request.query_params.get('cat_id')
        return Product.objects.filter(sub_category_id=prod_cat_id)


class ProductGetView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"


class ImagesGetView(RetrieveAPIView):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()
    lookup_field = "name"

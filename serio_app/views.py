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
    queryset = Category.objects.all()


class AnalogListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(analog=self.request.query_params.get("prod_id"))

class ProductSearchView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        lang, option = self.request.query_params.get('lang'),  self.request.query_params.get('option')
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
        return Product.objects.filter(category_id=prod_cat_id)


class ProductGetView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"

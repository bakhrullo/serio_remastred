from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/user/create/', UserCreateView.as_view()),
    path('api/v1/user/update/<int:tg_id>', UserUpdateView.as_view()),
    path('api/v1/user/get/<int:tg_id>', UserGetView.as_view()),
    path('api/v1/brock/get', BrockListView.as_view()),
    path('api/v1/region/get', RegionListView.as_view()),
    path('api/v1/service/get', ServiceListView.as_view()),
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/analog/', AnalogListView.as_view()),
    path('api/v1/product/', ProductListView.as_view()),
    path('api/v1/product/search', ProductSearchView.as_view()),
    path('api/v1/product/<int:id>', ProductGetView.as_view()),
]

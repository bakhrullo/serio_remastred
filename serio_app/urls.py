from django.urls import path

from .views import *

urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/update/<int:tg_id>', UserUpdateView.as_view()),
    path('user/get/<int:tg_id>', UserGetView.as_view()),
    path('brock/get', BrockListView.as_view()),
    path('region/get', RegionListView.as_view()),
    path('service/get', ServiceListView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('analog/', AnalogListView.as_view()),
    path('analog_type/', AnalogTypeListView.as_view()),
    path('product/', ProductListView.as_view()),
    path('product/search', ProductSearchView.as_view()),
    path('product/<int:id>', ProductGetView.as_view()),
    path('images/<str:name>', ImagesGetView.as_view())]

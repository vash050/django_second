from django.urls import re_path

import mainapp.views as mainapp

from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    re_path(r"^$", mainapp.products, name="index"),
    # path("", mainapp.products, name="index"),
    re_path(r"^category/(?P<pk>\d+)/$", mainapp.products, name="category"),
    # path("category/<int:pk>/", mainapp.products, name="category"),
    re_path(r"^category/(?P<pk>\d+)/page/(?P<page>\d+)/$", mainapp.products, name="page"),
    # path("category/<int:pk>/page/<int:page>/", mainapp.products, name="page"),
    re_path(r"^product/(?P<pk>\d+)/$", mainapp.product, name="product"),
    # path("product/<int:pk>/", mainapp.product, name="product"),
]

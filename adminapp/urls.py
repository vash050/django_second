from django.urls import re_path

import adminapp.views as adminapp

from .apps import AdminappConfig

app_name = AdminappConfig.name

urlpatterns = [
    re_path(r"^$", adminapp.admin_main, name="admin_main"),
    # path("", adminapp.admin_main, name="admin_main"),
    re_path(r"^users/create/$", adminapp.user_create, name="user_create"),
    # path("users/create/", adminapp.user_create, name="user_create"),
    re_path(r"^users/read/$", adminapp.UsersListView.as_view(), name="users"),
    # path("users/read/", adminapp.UsersListView.as_view(), name="users"),
    re_path(r"^users/update/(?P<pk>\d+)/$", adminapp.user_update, name="user_update"),
    # path("users/update/<int:pk>/", adminapp.user_update, name="user_update"),
    re_path(r"^users/delete/(?P<pk>\d+)/$", adminapp.user_delete, name="user_delete"),
    # path("users/delete/<int:pk>/", adminapp.user_delete, name="user_delete"),
    re_path(r"^categories/create/$", adminapp.ProductCategoryCreateView.as_view(), name="category_create"),
    # path("categories/create/", adminapp.ProductCategoryCreateView.as_view(), name="category_create"),
    re_path(r"^categories/read/$", adminapp.categories, name="categories"),
    # path("categories/read/", adminapp.categories, name="categories"),
    re_path(r"^categories/update/(?P<pk>\d+)/$", adminapp.ProductCategoryUpdateView.as_view(), name="category_update"),
    # path("categories/update/<int:pk>/", adminapp.ProductCategoryUpdateView.as_view(), name="category_update"),
    re_path(r"^categories/delete/(?P<pk>\d+)/$", adminapp.ProductCategoryDeleteView.as_view(), name="category_delete"),
    # path("categories/delete/<int:pk>/", adminapp.ProductCategoryDeleteView.as_view(), name="category_delete"),
    re_path(r"^products/create/category/(?P<pk>\d+)/$", adminapp.product_create, name="product_create"),
    # path("products/create/category/<int:pk>/", adminapp.product_create, name="product_create"),
    re_path(r"^products/read/category/(?P<pk>\d+)/$", adminapp.products, name="products"),
    # path("products/read/category/<int:pk>/", adminapp.products, name="products"),
    re_path(r"^products/read/(?P<pk>\d+)/$", adminapp.ProductDetailView.as_view(), name="product_read"),
    # path("products/read/<int:pk>/", adminapp.ProductDetailView.as_view(), name="product_read"),
    re_path(r"^products/update/(?P<pk>\d+)/$", adminapp.product_update, name="product_update"),
    # path("products/update/<int:pk>/", adminapp.product_update, name="product_update"),
    re_path(r"^products/delete/(?P<pk>\d+)/$", adminapp.product_delete, name="product_delete"),
    # path("products/delete/<int:pk>/", adminapp.product_delete, name="product_delete"),
]

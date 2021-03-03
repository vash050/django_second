from django.urls import path, re_path

import authnapp.views as authnapp
# from authnapp.apps import AuthnappConfig

app_name = "authnapp"  # имя в уроке AuthapppConfig.name

urlpatterns = [
    re_path(r"^login/$", authnapp.login, name="login"),
    # path("login/", authnapp.login, name="login"),
    re_path(r"^logout/$", authnapp.logout, name="logout"),
    # path("logout/", authnapp.logout, name="logout"),
    re_path(r"^register/$", authnapp.register, name="register"),
    # path("register/", authnapp.register, name="register"),
    re_path(r"^edit/$", authnapp.edit, name="edit"),
    # path("edit/", authnapp.edit, name="edit"),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authnapp.verify, name='verify'),
]

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),
    re_path(r'^cargos/$', views.CargoList.as_view(), name='cargo-list'),

]
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),
    re_path(r'^cargos/$', views.CargoList.as_view(), name='cargo-list'),
    re_path(r'^tipos/$', views.TipoList.as_view(), name='tipo-list'),
    re_path(r'^componentes/$', views.ComponenteList.as_view(), name='componente-list'),
    re_path(r'^kits/$', views.KitList.as_view(), name='kit-list'),
    re_path(r'^kit-componentes/$', views.KitComponenteList.as_view(), name='kitcomponente-list'),
    re_path(r'^historico-producao/$', views.HistoricoProducaoList.as_view(), name='historicoproducao-list'),
    re_path('consumir-servico-ia/', views.ConsumirServicoIA.as_view(), name='consumir-servico-ia'),
]
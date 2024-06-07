from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CargoList(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class TipoList(generics.ListCreateAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class ComponenteList(generics.ListCreateAPIView):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

class KitList(generics.ListCreateAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

class KitComponenteList(generics.ListCreateAPIView):
    queryset = KitComponente.objects.all()
    serializer_class = KitComponenteSerializer

class HistoricoProducaoList(generics.ListCreateAPIView):
    queryset = HistoricoProducao.objects.all()
    serializer_class = HistoricoProducaoSerializer

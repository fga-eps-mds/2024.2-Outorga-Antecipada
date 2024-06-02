from rest_framework import generics
from .models import Usuario, Cargo
from .serializers import UsuarioSerializer, CargoSerializer

# Create your views here.
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CargoList(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
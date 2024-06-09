from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import base64
import json
from .models import *
from .serializers import *

IA_API_URL = "http://127.0.0.1:8080/IA"

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

class ConsumirServicoIA(APIView):
    def get(self, request, format=None):
        try:
            response = requests.get(IA_API_URL)

            if response.status_code == 200:
                data = json.loads(response.content)

                decoded_binary_data_image = base64.b64decode(data["image"])
                classes_identificadas = data.get("classesIdentificadas", [])
                confianca = data.get("confianca", [])

                with open('restored_image.jpg', 'wb') as file:
                    file.write(decoded_binary_data_image)
                return Response({"classes_identificadas": classes_identificadas, "confianca": confianca }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Erro ao acessar a API de IA"}, status=response.status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class KitsAgrupados(APIView):
    def get(self, request, format=None):
        kits_agrupados = []
        kits = Kit.objects.all()

        for kit in kits:
            composicoes_kit = KitComponente.objects.filter(id_kit=kit)
            quantidade_peca_total = 0
            componentes = []

            for composicao_kit in composicoes_kit:
                componente = composicao_kit.id_componente
                quantidade = composicao_kit.qtd_pecas
                quantidade_peca_total += quantidade
                componentes.append({
                    'id_componente': componente.id,
                    'nome': componente.nome,
                    'tipo': componente.id_tipo.nome,
                    'quantidade': quantidade
                })

            kits_agrupados.append({
                'id_kit': kit.id,
                'componentes': componentes,
                'quantidade_peca_total': quantidade_peca_total
            })

        return Response(kits_agrupados)
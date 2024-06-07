from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cargo
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Componente
        fields = '__all__'

class KitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kit
        fields = '__all__'

class KitComponenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = KitComponente
        fields = '__all__'

class HistoricoProducaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricoProducao
        fields = '__all__'

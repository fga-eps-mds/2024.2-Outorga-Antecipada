from rest_framework import serializers
from .models import Usuario, Cargo

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cargo
        fields = '__all__'
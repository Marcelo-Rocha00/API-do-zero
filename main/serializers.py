from rest_framework import serializers
from .models import Item, Funcionarios

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class FuncionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'
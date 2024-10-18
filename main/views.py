from rest_framework import viewsets
from .models import Item, Funcionarios
from .serializers import ItemSerializers, FuncionarioSerializers

class ItemViewsets(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class FuncionarioViewsets(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionarioSerializers
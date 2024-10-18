from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewsets, FuncionarioViewsets

router = DefaultRouter()
router.register(r"Item", ItemViewsets)
router.register(r"Funcionario", FuncionarioViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
    
]

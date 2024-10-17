from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewsets



router = DefaultRouter()
router.register(r"Item", ItemViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
    
]

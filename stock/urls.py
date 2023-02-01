from django.urls import path
from .views import PurchasesView, SalesView, ProductView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("purchases", PurchasesView)
router.register("sales", SalesView)
router.register("product", ProductView)

urlpatterns = [
    
]
urlpatterns += router.urls
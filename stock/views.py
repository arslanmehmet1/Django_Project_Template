from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
from .permissions import IsStaffOrReadOnly

class PurchasesView(ModelViewSet):
    queryset=Purchases.objects.all()
    serializer_class=PurchaseSerializer
    permission_classes=(IsStaffOrReadOnly,)

class SalesView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = (IsStaffOrReadOnly,)


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsStaffOrReadOnly,)


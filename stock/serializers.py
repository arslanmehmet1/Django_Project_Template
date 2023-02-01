from rest_framework import serializers
from .models import *

class PurchaseSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = (
            'user',
            'firm',
            'brand',
            'product',
            'quantity',
            'price',
            'total_price'
        )
    def get_total_price(self, obj):
        return obj.quantity * obj.price

class SalesSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Sales
        fields = (
            'user',
            'brand',
            'product',
            'quantity',
            'price',
            'total_price'
        )
    def get_total_price(self, obj):
        return obj.quantity * obj.price

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'brand',
            'stock',
            'created_date',
            'updated_date'
        )


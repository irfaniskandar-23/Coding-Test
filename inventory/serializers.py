from rest_framework import serializers
from inventory.models import Supplier, Inventory


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name')

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'note',
                  'stock', 'availiability', 'supplier_name']


class QuerySerializer(serializers.ModelSerializer):
    model = Inventory
    fields = ['id', 'name',  'availiability', 'supplier_name']

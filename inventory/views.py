import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404

# import from serializer
from inventory.models import Supplier, Inventory
from inventory.serializers import InventorySerializer, QuerySerializer

# rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer


class InventoryList(APIView):
    '''
    list all inventory
    '''

    def get(self, request, format=None):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self, request, *args, **kwargs):
        id = request.query_params['id']

        if id is not None:
            inventory = Inventory.objects.get(id=id)
            serializer = QuerySerializer(inventory)
        else:
            inventory = self.get_queryset()
            serializer = QuerySerializer(inventory, many=True)

        return Response(serializer.data)


class InventoryDetail(APIView):
    '''
    retrieve specific inventory item
    '''

    def get_item(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventory = self.get_item(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data, status=status.HTTP_200_OK)


def ViewInventory(request):
    response = requests.get('http://127.0.0.1:8000/api/inventory/').json()
    return render(request, 'view.html', {'response': response}, status=status.HTTP_200_OK)


def ViewInventoryDetail(request, pk):
    response = requests.get(f'http://127.0.0.1:8000/api/inventory/{pk}')
    data = response.json()

    if response.status_code == 200:
        return render(request, 'inventory_detail.html', {'response': data}, status=status.HTTP_200_OK)

    else:
        raise Http404

from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # api/products
        pass

    def create(self, request):
        pass

    def retrieve(self, pk=None):
        pass
    def update(self, pk=None):
        pass
    def delete(self, pk=None):
        pass

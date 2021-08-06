from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product

class ProductApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
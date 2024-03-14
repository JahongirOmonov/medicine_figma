from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from shop import serializers
from .models import Product, Category
from rest_framework.views import APIView
from .cart import Cart
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer

class CartApiView(APIView):
    def get(self, request):
        cart = Cart(request)
        return Response(cart.cart)


class RemoveFromCartApiView(APIView):
    def post(self, request, id, *args, **kwargs):
        cart = Cart(request)
        cart.remove(id)
        return Response({"message": "Product removed from cart"})



class ClearCartApiView(APIView):
    def post(self, request, format=None):
        cart = Cart(request)
        try:

            cart.save_clear()
            return Response({"message": "Cart cleared successfully"})
        except KeyError:
            return Response({"error": "Cart does not exist."})


class Total_sum(APIView):
    def get(self, request, format=None):
        cart = Cart(request)
        x = cart.calculate_total_sum()
        return Response({"Total sum": f"{x}"})


class CategorySearchListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('id', 'title')
    filterset_fields = ('id', 'title')

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
import logging
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class LoginView(generics.GenericAPIView):
    
    def post(self, request, *args,  **kwargs):
        pass
        

class DashboardView(APIView):
    def get(self, request, *args,  **kwargs):
        # Возвращаем список доступных уровней логирования
        logger.info('Call to /api/dashboard!')
        return Response({'message': 'Hello, world!'})

class OrdersView(APIView):
    def get(self, request, *args,  **kwargs):
        return Response({'message': 'Hello, world!'})
    def post(self, request, *args,  **kwargs):
        pass

class PaymentsView(generics.GenericAPIView):
    def get(self, request, *args,  **kwargs):
        pass
    def post(self, request, *args,  **kwargs):
        pass

class ProductsView(generics.GenericAPIView):
    def get(self, request, *args,  **kwargs):
        pass
    def post(self, request, *args,  **kwargs):
        pass

class ShippingView(generics.GenericAPIView):
    def get(self, request, *args,  **kwargs):
        pass
    def post(self, request, *args,  **kwargs):
        pass


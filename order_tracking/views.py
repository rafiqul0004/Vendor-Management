from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.

class OrderTrackingViewSet(viewsets.ModelViewSet):
    queryset=models.PurchaseOrder.objects.all()
    serializer_class = serializers.OrderTrackingSerializers
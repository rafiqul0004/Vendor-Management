from rest_framework import serializers
from .import models

class OrderTrackingSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.PurchaseOrder
        fields='__all__'
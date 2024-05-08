from rest_framework import viewsets
from .models import Vendor,HistoricalPerformance
from .serializers import VendorPerformanceSerializer,HistoricalPerformanceSerializer

class VendorPerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
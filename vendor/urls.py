from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Define a router for the vendor API
vendor_router = DefaultRouter()
vendor_router.register(r'vendors', views.VendorPerformanceViewSet)

# Define a router for the performance API
performance_router = DefaultRouter()
performance_router.register(r'performance', views.HistoricalPerformanceViewSet)

urlpatterns = [
    path('api/', include(vendor_router.urls)),  
    path('api/performance/', include(performance_router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'purchase_orders', views.OrderTrackingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

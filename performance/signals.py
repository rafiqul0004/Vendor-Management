# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from vendor.models import Vendor
# from .models import HistoricalPerformance

# @receiver(post_save, sender=Vendor)
# def create_historical_performance(sender, instance, created, **kwargs):
#     if created:
#         HistoricalPerformance.objects.create(
#             vendor=instance,
#             on_time_delivery_rate=instance.on_time_delivery_rate,
#             quality_rating_avg=instance.quality_rating_avg,
#             average_response_time=instance.average_response_time,
#             fulfillment_rate=instance.fulfillment_rate
#         )

from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def update_performance_metrics(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()

        #on-time delivery rate
        if total_completed_pos > 0:
            on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('expected_delivery_date')).count()
            self.on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100
        else:
            self.on_time_delivery_rate = 0.0

        # quality rating average
        completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
        if completed_pos_with_rating.exists():
            self.quality_rating_avg = completed_pos_with_rating.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
        else:
            self.quality_rating_avg = 0.0

        # average response time
        acknowledged_pos = completed_pos.exclude(acknowledgment_date__isnull=True)
        if acknowledged_pos.exists():
            total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
            self.average_response_time = total_response_time / acknowledged_pos.count() / 3600  # in hours
        else:
            self.average_response_time = 0.0

        # fulfilment rate
        fulfilled_pos = completed_pos.filter(issues__isnull=True)
        if total_completed_pos > 0:
            self.fulfillment_rate = (fulfilled_pos.count() / total_completed_pos) * 100
        else:
            self.fulfillment_rate = 0.0

        self.save()

    def __str__(self):
        return self.name
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
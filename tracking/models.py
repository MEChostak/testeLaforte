from django.db import models
import json


class Tracking(models.Model):
    tracking_number = models.CharField(max_length=40, null=False, blank=False)
    order_id = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "Tracking"

    def __str__(self):
        return self.tracking_number, self.order_id


def create_json(self):
    data = {
        "location_id": 123456789,
        "order_id": self.order_id,
        "tracking_number": self.tracking_number,
        "tracking_urls": "http://www.correios.com.br/rastreamento"}
    json_data = json.dumps(data)
    return data

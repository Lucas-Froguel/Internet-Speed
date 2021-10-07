from django.db import models
from internet_speed.mixins import ModelMixin


class Internet(ModelMixin):
    class Meta:
        db_table = "internet"
        ordering = ("created_at",)

    download_speed = models.FloatField(default=0)
    upload_speed = models.FloatField(default=0)
    ping = models.FloatField(default=0)
    image_url = models.URLField(default="")

    def __str__(self):
        return "Internet Speed"










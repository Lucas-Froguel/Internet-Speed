from internet_speed.models import Internet
from django.db import connection


def add_speed_data_to_db(speed_data):

    Internet.objects.create(download_speed=speed_data["download"],
                            upload_speed=speed_data["upload"],
                            ping=speed_data["ping"],
                            image_url=speed_data["share"])


def get_data_from_db(now, last_week):
    data = Internet.objects.filter(created_at__gte=last_week)
    data = data.filter(created_at__lte=now).values()

    return data

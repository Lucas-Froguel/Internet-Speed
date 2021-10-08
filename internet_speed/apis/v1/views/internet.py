from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from internet_speed.speed_test.speed_test import get_speed
from internet_speed.utils.db_utils import add_speed_data_to_db
from internet_speed.cron.send_email import send_email


@api_view(["GET"])
def get_internet_speed_view(request):
    if request.method == "GET":
        speed = get_speed()

        return Response(speed, status=200)


@api_view(["POST"])
def add_data_db_now_view(request):
    if request.method == "POST":
        speed = get_speed()
        add_speed_data_to_db(speed)

        return Response(status=201)


@api_view(["GET"])
def send_email_view(request):
    if request.method == "GET":
        send_email()

        return Response(status=200)

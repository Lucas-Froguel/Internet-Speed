from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from internet_speed.speed_test.speed_test import get_speed


@api_view(["GET"])
def get_internet_speed_view(request):
    if request.method == "GET":
        speed = get_speed()
        speed["download"] = speed["download"] / 10**6
        speed["upload"] = speed["upload"] / 10 ** 6
        return Response(speed, status=200)

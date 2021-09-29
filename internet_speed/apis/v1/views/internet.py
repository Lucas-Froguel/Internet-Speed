from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_internet_speed_view(request):
    if request.method == "GET":
        pass

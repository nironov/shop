from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.core.postgresql_connection import cur, conn
from .serializers import DataSerializer
from .utils import get_most_viewed_products_from_db


@api_view(['GET'])
def get_data(request):
    # извлечь из request то, что нужно найти в БД
    get_most_viewed_products_from_db()

    # в аргументы сериалайзера передать обьект с найденными обьектами из БДб
    # many=True если обьектов несколько, если один many=False
    # serializer = DataSerializer(res, many=True)

    # в ответ serializer.data
    return Response(200)

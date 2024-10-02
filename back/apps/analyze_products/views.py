from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.core.postgresql_connection import cur, conn
from .serializers import DataSerializer
from .utils import get_most_viewed_products_by_id, popular_products_in_list

import redis
import pickle


@api_view(['GET'])
def get_data(request):
    if 'new_popular_products' in request.data:
        popular_products_in_list()

        return Response(200)

    if 'get_popular_products' in request.data:

        red = redis.Redis()
        serialized_data_from_redis = pickle.loads(red.get('products_data'))
        serializer = DataSerializer(serialized_data_from_redis)
        print('FULL SERIALIZED DATA', serialized_data_from_redis, type(serialized_data_from_redis))
        print('UNPICKLED DATA', serialized_data_from_redis[0], type(serialized_data_from_redis[0]))
        return Response(serializer.data)

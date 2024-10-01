from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.core.postgresql_connection import cur, conn
from .serializers import DataSerializer
from .utils import get_most_viewed_products_by_id, popular_products_in_list




@api_view(['GET'])
def get_data(request):
    if 'new_popular_products' in request.data:
        data = popular_products_in_list()
        print('REQUEST.DATA', request.data, type(request.data))
        print('REQUEST.DATA', dict(request.data))

        print('NEW DATA', data)
        serializer = DataSerializer(data)

        return Response(serializer.data)

    if 'get_popular_products' in request.data:
        # нужна переменная, котоая будет хранить инфо о товарах, без повторного запроса в БД
        # return Response(old_products)
        # TODO: товары хранятся в кэше редиса, но есть ошибка MultiValueDictKeyError: 'new_popular_products'
        import redis
        import pickle
        red = redis.Redis()
        data_to_serialize = pickle.loads(red.get('products_data'))
        serializer = DataSerializer(data_to_serialize[0])
        print('UNPICKLED DATA', data_to_serialize[0], type(data_to_serialize[0]))
        return Response(serializer.data)

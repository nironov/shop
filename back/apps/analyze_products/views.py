from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    asnwer = {'key1': 'value1', 'key2': 'value2'}
    return Response(asnwer)

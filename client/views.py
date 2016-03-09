from django.shortcuts import render
from django.db import connection, transaction
from client.serialize import PowerSerializer, PowerListSerializer, \
    DBChangesSerializer
from client.models import Power, DBChanges
from client.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, response, status, settings, decorators
import time
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


class PowerViewSet(viewsets.ModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def list(self, request, *args, **kwargs):
            queryset = Power.objects.all()
            serializer = PowerListSerializer(queryset, many=True)
            return response.Response(serializer.data)

    @decorators.detail_route(methods=['post'])
    def new_node(self, request, **kwargs):
        serializer = PowerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(data=None,
                                 status=status.HTTP_201_CREATED,
                                 headers=headers)

    def perform_create(self, serializer):
        logger.info("attempting to add")
        cursor = connection.cursor()
        cursor.execute('update client_dbchanges set update_check=' +
                                  str(time.time())+' where id = 1')
        transaction.commit()
        cursor.close()
        logger.info("wrote to db in create")
        serializer.save()

    def perform_update(self, serializer):
        logger.info("attempting to update")
        cursor = connection.cursor()
        cursor.execute('update client_dbchanges set update_check=' +
                                  str(time.time())+' where id = 1')
        transaction.commit()
        cursor.close()
        logger.info("wrote to db in update")
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[settings.api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}


class DBChangeViewSet(viewsets.ModelViewSet):
    queryset = DBChanges.objects.all()
    serializer_class = DBChangesSerializer
    permission_classes = (IsOwnerOrReadOnly,)

from django.shortcuts import render
from django.db import connection, transaction
from django.shortcuts import get_object_or_404
from client.serialize import LoadSerializer, NodeListSerializer, \
    DBChangesSerializer, SyncGeneratorSerializer, BusSerializer, \
    UtilitySerializer
from client.models import Load, DBChanges, Node, SyncGenerator, Utility, Bus
from client.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, response, status, settings, decorators
import time
import logging
from . import constants as const

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Node.objects.all()
        node = get_object_or_404(queryset, pk=pk)
        node_type = node.type
        queryset = get_query_set(node_type)
        node = get_object_or_404(queryset, pk=node.f_id)
        serializer = get_serializer(node_type, node)
        return response.Response(serializer.data)

    def list(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute('select n.id, foo.name, n.type FROM client_node n, '
                       '(select name from client_load UNION select name from '
                       'client_syncgenerator UNION select name from client_bus '
                       'UNION select name from client_utility) as foo where '
                       'foo.name = ((SELECT l.name from client_load l where '
                       'n.type = 0 and n.f_id = l.id) UNION (SELECT sg.name '
                       'FROM client_syncgenerator sg WHERE n.type = 1 and '
                       'n.f_id = sg.id) UNION (SELECT b.name FROM client_bus b '
                       'WHERE n.type = 2 and n.f_id = b.id) UNION '
                       '(SELECT u.name FROM client_utility u WHERE n.type = 3 '
                       'and n.f_id = u.id))')
        data = dictfetchall(cursor)
        serializer = NodeListSerializer(data, many=True)
        return response.Response(serializer.data)

class NodeMarkerViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeListSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Node.objects.all()
        node = get_object_or_404(queryset, pk=pk)
        node_type = node.type
        queryset = get_query_set(node_type)
        node = get_object_or_404(queryset, pk=node.f_id)
        serializer = get_serializer(node_type, node)
        return response.Response(serializer.data)

    def list(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute('select n.id, foo.name, n.type, n.latitude, n.longitude FROM client_node n, '
                       '(select name from client_load UNION select name from '
                       'client_syncgenerator UNION select name from client_bus '
                       'UNION select name from client_utility) as foo where '
                       'foo.name = ((SELECT l.name from client_load l where '
                       'n.type = 0 and n.f_id = l.id) UNION (SELECT sg.name '
                       'FROM client_syncgenerator sg WHERE n.type = 1 and '
                       'n.f_id = sg.id) UNION (SELECT b.name FROM client_bus b '
                       'WHERE n.type = 2 and n.f_id = b.id) UNION '
                       '(SELECT u.name FROM client_utility u WHERE n.type = 3 '
                       'and n.f_id = u.id))')
        data = dictfetchall(cursor)
        serializer = NodeListSerializer(data, many=True)
        return response.Response(serializer.data)

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def list(self, request, *args, **kwargs):
        queryset = Load.objects.all()
        serializer = LoadSerializer(queryset, many=True)
        return response.Response(serializer.data)

    @decorators.detail_route(methods=['post'])
    def new_node(self, request, **kwargs):
        serializer = LoadSerializer(data=request.data)
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
        logger.info(serializer.data)
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


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_query_set(node_type):
    if node_type == const.LOAD:
        return Load.objects.all()
    elif node_type == const.SYNC_GENERATOR:
        return SyncGenerator.objects.all()
    elif node_type == const.BUS:
        return Bus.objects.all()
    elif node_type == const.UTILITY:
        return Utility.objects.all()


def get_serializer(node_type, node):
    if node_type == const.LOAD:
        return LoadSerializer(node)
    elif node_type == const.SYNC_GENERATOR:
        return SyncGeneratorSerializer(node)
    elif node_type == const.BUS:
        return BusSerializer(node)
    elif node_type == const.UTILITY:
        return UtilitySerializer(node)

'''
long ass query I'm not ready to part with yet:
select n.id, foo.name, n.type FROM client_node n, (select name from client_load
UNION select name from client_syncgenerator UNION select name from client_bus
UNION select name from client_utility) as foo where foo.name = ((SELECT l.name
from client_load l where n.type = 0 and n.f_id = l.id) UNION (SELECT sg.name
FROM client_syncgenerator sg WHERE n.type = 1 and n.f_id = sg.id) UNION
(SELECT b.name FROM client_bus b WHERE n.type = 2 and n.f_id = b.id) UNION
(SELECT u.name FROM client_utility u WHERE n.type = 3 and n.f_id = u.id))
'''

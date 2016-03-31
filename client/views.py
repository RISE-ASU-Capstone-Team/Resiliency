from django.shortcuts import render
from django.db import connection, transaction
from django.shortcuts import get_object_or_404
from client.serialize import LoadSerializer, DBChangesSerializer, \
    SyncGeneratorSerializer, BusSerializer, \
    UtilitySerializer, NodeMarkerSerializer, ConnectionListSerializer, \
    TwoWindingTransformerSerializer, DirectConnectionSerializer, \
    CableSerializer, OverheadLineSerializer, PowerSerializer, \
    WireDataSerializer, LineCodeSerializer, ReservoirSerializer, \
    PipeSerializer
from client.models import Connection, Load, DBChanges, Node, SyncGenerator, \
    Utility, Bus, TwoWindingTransformer, DirectConnection, Cable, OverheadLine, \
    Power, WireData, LineCode, Reservoir, Pipe
from client.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, response, status, settings, decorators
import time
import logging
from . import constants as const

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


class NodeMarkerViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeMarkerSerializer
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
        cursor.execute('select n.id, n.name, n.type, n.latitude, n.longitude '
                       'FROM client_node n')
        data = dict_fetch_all(cursor)
        serializer = NodeMarkerSerializer(data, many=True)
        return response.Response(serializer.data)


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionListSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# ------------------------------------------------------------------ Power Nodes
class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class SyncGenViewSet(viewsets.ModelViewSet):
    queryset = SyncGenerator.objects.all()
    serializer_class = SyncGeneratorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class UtilityViewSet(viewsets.ModelViewSet):
    queryset = Utility.objects.all()
    serializer_class = UtilitySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


# ------------------------------------------------------------ Power Connections
class TwoWindingTransformerViewSet(viewsets.ModelViewSet):
    queryset = TwoWindingTransformer.objects.all()
    serializer_class = TwoWindingTransformerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class DirectConnectionViewSet(viewsets.ModelViewSet):
    queryset = DirectConnection.objects.all()
    serializer_class = DirectConnectionSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class CableViewSet(viewsets.ModelViewSet):
    queryset = Cable.objects.all()
    serializer_class = CableSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


class OverheadLineViewSet(viewsets.ModelViewSet):
    queryset = OverheadLine.objects.all()
    serializer_class = OverheadLineSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


# ----------------------------------------------------------- Power
class PowerViewSet(viewsets.ModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        data = []
        new_data = dict()
        new_data['bus_count'] = Bus.objects.count()
        new_data['utility_count'] = Utility.objects.count()
        new_data['generator_count'] = SyncGenerator.objects.count()
        new_data['load_count'] = Load.objects.count()
        new_data['transformer_count'] = TwoWindingTransformer.objects.count()
        new_data['branch_count'] = 0
        data.append(new_data)
        serializer = PowerSerializer(data, many=True)
        return response.Response(serializer.data)


class WireDataViewSet(viewsets.ModelViewSet):
    queryset = WireData.objects.all()
    serializer_class = WireDataSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class LineDataViewSet(viewsets.ModelViewSet):
    queryset = LineCode.objects.all()
    serializer_class = LineCodeSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# ------------------------------------------------------------------ Water Nodes
class ReservoirViewSet(viewsets.ModelViewSet):
    queryset = Reservoir.objects.all()
    serializer_class = ReservoirSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


# ------------------------------------------------------------ Water Connections
class PipeViewSet(viewsets.ModelViewSet):
    queryset = Pipe.objects.all()
    serializer_class = PipeSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        update_made()
        serializer.save()

    def perform_update(self, serializer):
        update_made()
        serializer.save()

    def perform_destroy(self, instance):
        update_made()
        instance.delete()


# -------------------------------------------------------------------- DB Update
class DBChangeViewSet(viewsets.ModelViewSet):
    queryset = DBChanges.objects.all()
    serializer_class = DBChangesSerializer
    permission_classes = (IsOwnerOrReadOnly,)


def dict_fetch_all(cursor):
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
    elif node_type == const.RESERVOIR:
        return Reservoir.objects.all()


def get_serializer(node_type, node):
    if node_type == const.LOAD:
        return LoadSerializer(node)
    elif node_type == const.SYNC_GENERATOR:
        return SyncGeneratorSerializer(node)
    elif node_type == const.BUS:
        return BusSerializer(node)
    elif node_type == const.UTILITY:
        return UtilitySerializer(node)
    elif node_type == const.RESERVOIR:
        return ReservoirSerializer(node)


def update_made():
    cursor = connection.cursor()
    cursor.execute('update client_dbchanges set update_check=' +
                   str(time.time())+' where id = 1')
    transaction.commit()
    cursor.close()

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

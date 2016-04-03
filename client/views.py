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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        cursor = connection.cursor()
        cursor.execute('select nominal_voltage '
                       'FROM client_node where id = ' + request.data['id'])
        data = dict_fetch_all(cursor)
        cursor.close()
        if float(request.data['nominal_voltage']) != float(data[0]['nominal_voltage']):
            change_voltage(request.data['id'], request.data['nominal_voltage'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        cursor = connection.cursor()
        cursor.execute('select nominal_voltage '
                       'FROM client_node where id = ' + request.data['id'])
        data = dict_fetch_all(cursor)
        cursor.close()
        if float(request.data['nominal_voltage']) != float(data[0]['nominal_voltage']):
            change_voltage(request.data['id'], request.data['nominal_voltage'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        cursor = connection.cursor()
        cursor.execute('select nominal_voltage '
                       'FROM client_node where id = ' + request.data['id'])
        data = dict_fetch_all(cursor)
        cursor.close()
        if float(request.data['nominal_voltage']) != float(data[0]['nominal_voltage']):
            change_voltage(request.data['id'], request.data['nominal_voltage'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        cursor = connection.cursor()
        cursor.execute('select nominal_voltage '
                       'FROM client_node where id = ' + request.data['id'])
        data = dict_fetch_all(cursor)
        cursor.close()
        if float(request.data['nominal_voltage']) != float(data[0]['nominal_voltage']):
            change_voltage(request.data['id'], request.data['nominal_voltage'])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

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
    if node_type == const.Power.LOAD:
        return Load.objects.all()
    elif node_type == const.Power.SYNCHRONOUS_GENERATOR:
        return SyncGenerator.objects.all()
    elif node_type == const.Power.BUS:
        return Bus.objects.all()
    elif node_type == const.Power.UTILITY:
        return Utility.objects.all()
    elif node_type == const.Water.RESERVOIR:
        return Reservoir.objects.all()


def get_serializer(node_type, node):
    if node_type == const.Power.LOAD:
        return LoadSerializer(node)
    elif node_type == const.Power.SYNCHRONOUS_GENERATOR:
        return SyncGeneratorSerializer(node)
    elif node_type == const.Power.BUS:
        return BusSerializer(node)
    elif node_type == const.Power.UTILITY:
        return UtilitySerializer(node)
    elif node_type == const.Water.RESERVOIR:
        return ReservoirSerializer(node)


def update_made():
    cursor = connection.cursor()
    cursor.execute('update client_dbchanges set update_check=' +
                   str(time.time())+' where id = 1')
    transaction.commit()
    cursor.close()


def change_voltage(node_id, voltage):
    # Change node voltage
    cursor = connection.cursor()
    logger.info("changing node " + str(node_id))
    cursor.execute('update client_node set nominal_voltage = ' + str(voltage) +
                   ' where id = ' + str(node_id))
    cursor.execute('select id, type from client_connection '
                   'where from_bus_id = ' + str(node_id))
    data = dict_fetch_all(cursor)
    # For each connection - from
    for x in range(len(data)):
        cont, next_node = update_connection_voltage(cursor, data[x], voltage, False)
        if cont and next_node != -1:
            cursor.close()
            change_voltage(next_node, voltage)

    cursor.execute('select id, type from client_connection '
                   'where to_bus_id = ' + str(node_id))
    data = dict_fetch_all(cursor)
    # For each connection - to
    for x in range(len(data)):
        cont, next_node = update_connection_voltage(cursor, data[x], voltage, True)
        cursor.close()
        if cont:
            change_voltage(next_node, voltage)


def update_connection_voltage(cursor, data, voltage, to):
    current_con_id = data['id']
    logger.info("changing con " + str(current_con_id) + ' of type ' + str(data['type']))
    if data['type'] == const.Power.TWO_WINDING_TRANSFORMER:
        if to:
            cursor.execute('update client_twowindingtransformer '
                           'set to_bus_voltage_rating = ' + str(voltage) +
                           ' where connection_ptr_id = ' + str(current_con_id))
        else:
            cursor.execute('update client_twowindingtransformer '
                           'set from_bus_voltage_rating = ' + str(voltage) +
                           ' where connection_ptr_id = ' + str(current_con_id))
        return False, -1
    elif data['type'] == const.Power.DIRECT_CONNECTION:
        cursor.execute('select to_bus_voltage_rating '
                       'from client_directconnection '
                       'where connection_ptr_id = ' + str(current_con_id))
        data = dict_fetch_all(cursor)
        logger.info('Selected from direct rating: ' + str(data[0]['to_bus_voltage_rating']))
        if data[0]['to_bus_voltage_rating'] == voltage:
            return False, -1
        else:
            cursor.execute('update client_directconnection '
                           'set to_bus_voltage_rating = ' + str(voltage) +
                           ', from_bus_voltage_rating = ' + str(voltage) +
                           ' where connection_ptr_id = ' + str(current_con_id))
            logger.info('Executing direct update =======')
            if to:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select from_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting from bus in direct =======')
            else:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select to_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting to bus in direct =======')
        return True, next_node
    elif data['type'] == const.Power.CABLE:
        cursor.execute('select voltage_rating '
                       'from client_cable '
                       'where connection_ptr_id = ' + str(current_con_id))
        data = dict_fetch_all(cursor)
        logger.info('Selected from cable rating: ' + str(data[0]['voltage_rating']))
        if data[0]['voltage_rating'] == voltage:
            return False, -1
        else:
            cursor.execute('update client_cable '
                           'set voltage_rating = ' + str(voltage) +
                           ' where connection_ptr_id = ' + str(current_con_id))
            logger.info('Executing cable update =======')
            if to:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select from_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting from bus in cable =======')
            else:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select to_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting to bus in cable =======')
        return True, next_node
    elif data['type'] == const.Power.OVERHEAD_LINE:
        cursor.execute('select nominal_LL_voltage '
                       'from client_overheadline '
                       'where connection_ptr_id = ' + str(current_con_id))
        data = dict_fetch_all(cursor)
        logger.info('Selected from overhead voltage: ' + str(data[0]['nominal_LL_voltage']))
        if data[0]['nominal_LL_voltage'] == voltage:
            return False, -1
        else:
            cursor.execute('update client_overheadline '
                           'set nominal_LL_voltage = ' + str(voltage) +
                           ' where connection_ptr_id = ' + str(current_con_id))
            logger.info('Executing overhead update =======')
            if to:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select from_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting from bus in overhead =======')
            else:
                cursor.execute('select n.id from client_node n '
                               'where n.id = (select to_bus_id '
                               'from client_connection c where c.id = ' +
                               str(current_con_id) + ')')
                data = dict_fetch_all(cursor)
                next_node = data[0]['id']
                logger.info('Getting to bus in overhead =======')
        return True, next_node

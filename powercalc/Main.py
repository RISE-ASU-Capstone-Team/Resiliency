import Psycopg
from Constants import *


def main():
    nodes, connections, wire_data = Psycopg.populate_components()
    print(nodes)
    print(connections)
    '''
    connection1 = connections[next(iter(connections))]
    node1 = nodes[connection1['from_bus']]
    node2 = nodes[connection1['to_bus']]
    print("\n\n" + node1['name'] + " at lat: " + str(node1['latitude']) +
          " lon: " + str(node1['longitude']))
    print("\n\t\tis connected by " + connection1['name'] + ", which is a(n) " +
          get_connection_type(connection1['type']) + ", to")
    print("\n" + node2['name'] + " at lat: " + str(node2['latitude']) +
          " lon: " + str(node2['longitude']))

    if connection1['type'] == Power.OVERHEAD_LINE:
        print("\n\nWire Data for " + connection1['name'] + ":\n")
        print("\t\tname: " + wire_data[connection1['wiredata_object_id']].get('name') +
              '  type: ' + 'Phase' if wire_data[connection1['wiredata_object_id']].get('wire_type') == WireType.PHASE else 'Neutral')
        print("\t\tobject: " + str(wire_data[connection1['wiredata_object_id']]))
    '''
    for node in nodes:
        print(nodes[node]['type'])


def get_connection_type(con_type):

    if con_type == Power.TWO_WINDING_TRANSFORMER:
        return "Two Winding Transformer"
    elif con_type == Power.DIRECT_CONNECTION:
        return "Direct Connection"
    elif con_type == Power.CABLE:
        return "Cable"
    elif con_type == Power.OVERHEAD_LINE:
        return "Overhead Line"

if __name__ == '__main__':
    main()

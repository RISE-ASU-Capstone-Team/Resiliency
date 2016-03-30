import psycopg2
from powercalc.Constants import *


def populate_components():
    try:
        conn = psycopg2.connect("dbname='rise' user='admin' host='localhost' "
                                "port='3306' password='capstone'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()

    nodes = dict()
    populate_load(cur, nodes)
    populate_sync_gen(cur, nodes)
    populate_bus(cur, nodes)
    populate_utility(cur, nodes)

    connections = dict()
    populate_transformer(cur, connections)
    populate_direct(cur, connections)
    populate_cables(cur, connections)
    populate_overhead(cur, connections)

    wire_data = dict()
    populate_wire_data(cur, wire_data)

    line_codes = dict()
    populate_line_code(cur, line_codes)

    conn.close()
    return nodes, connections, wire_data, line_codes


def populate_load(cur, nodes):
    try:
        cur.execute("""SELECT * FROM public.client_node, public.client_load
                    WHERE
                    client_node.id = client_load.node_ptr_id""")
    except:
        print("I can't SELECT from load")

    rows = cur.fetchall()

    for row in rows:
        nodes[row[Load.ID]] = \
            {'id': row[Load.ID], 'name': row[Load.NAME],
             'operational_status': row[Load.OPERATIONAL_STATUS],
             'is_bus': row[Load.IS_BUS],
             'voltage_1_magnitude': row[Load.VOLTAGE_1_MAGNITUDE],
             'voltage_1_angle': row[Load.VOLTAGE_1_ANGLE],
             'voltage_1_pu': row[Load.VOLTAGE_1_PU],
             'type': row[Load.TYPE],
             'latitude': row[Load.LATITUDE],
             'longitude': row[Load.LONGITUDE],
             'power_rating': row[Load.POWER_RATING],
             'power_factor_percent': row[Load.POWER_FACTOR_PERCENT],
             'power_factor_type': row[Load.POWER_FACTOR_TYPE],
             'min_pu_voltage': row[Load.MIN_PU_VOLTAGE],
             'wiring': row[Load.WIRING],
             'load_model': row[Load.LOAD_MODEL],
             'current_rating': row[Load.CURRENT_RATING],
             'LL_voltage': row[Bus.LL_VOLTAGE],
             'nominal_voltage': row[Bus.NOMINAL_VOLTAGE],
             'current_1_magnitude': row[Load.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[Load.CURRENT_1_ANGLE],
             'real_power': row[Load.REAL_POWER],
             'reactive_power': row[Load.REACTIVE_POWER]}


def populate_sync_gen(cur, nodes):
    try:
        cur.execute("""SELECT * FROM public.client_node, public.client_syncgenerator
                    WHERE
                    client_node.id = client_syncgenerator.node_ptr_id""")
    except:
        print("I can't SELECT from syncgen")

    rows = cur.fetchall()

    for row in rows:
        nodes[row[SynchronousGenerator.ID]] = \
            {'id': row[SynchronousGenerator.ID], 
             'name': row[SynchronousGenerator.NAME],
             'operational_status': row[SynchronousGenerator.OPERATIONAL_STATUS],
             'is_bus': row[SynchronousGenerator.IS_BUS],
             'voltage_1_magnitude': row[SynchronousGenerator.VOLTAGE_1_MAGNITUDE],
             'voltage_1_angle': row[SynchronousGenerator.VOLTAGE_1_ANGLE],
             'voltage_1_pu': row[SynchronousGenerator.VOLTAGE_1_PU],
             'type': row[SynchronousGenerator.TYPE],
             'latitude': row[SynchronousGenerator.LATITUDE],
             'longitude': row[SynchronousGenerator.LONGITUDE],
             'stiffness': row[SynchronousGenerator.STIFFNESS],
             'power_rating': row[SynchronousGenerator.POWER_RATING],
             'RPM_rating': row[SynchronousGenerator.RPM_RATING],
             'number_of_poles': row[SynchronousGenerator.NUMBER_OF_POLES],
             'power_factor_percent': row[SynchronousGenerator.POWER_FACTOR_PERCENT],
             'wiring': row[SynchronousGenerator.WIRING],
             'LL_voltage': row[Bus.LL_VOLTAGE],
             'nominal_voltage': row[Bus.NOMINAL_VOLTAGE],
             'current_1_magnitude': row[SynchronousGenerator.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[SynchronousGenerator.CURRENT_1_ANGLE],
             'real_power': row[SynchronousGenerator.REAL_POWER],
             'reactive_power': row[SynchronousGenerator.REACTIVE_POWER]}


def populate_bus(cur, nodes):
    try:
        cur.execute("""SELECT * FROM public.client_node, public.client_bus
                    WHERE
                    client_node.id = client_bus.node_ptr_id""")
    except:
        print("I can't SELECT from bus")

    rows = cur.fetchall()

    for row in rows:
        nodes[row[Bus.ID]] = \
            {'id': row[Bus.ID], 
             'name': row[Bus.NAME],
             'operational_status': row[Bus.OPERATIONAL_STATUS],
             'is_bus': row[Bus.IS_BUS],
             'voltage_1_magnitude': row[Bus.VOLTAGE_1_MAGNITUDE],
             'voltage_1_angle': row[Bus.VOLTAGE_1_ANGLE],
             'voltage_1_pu': row[Bus.VOLTAGE_1_PU],
             'type': row[Bus.TYPE],
             'latitude': row[Bus.LATITUDE],
             'longitude': row[Bus.LONGITUDE],
             'LL_voltage': row[Bus.LL_VOLTAGE],
             'nominal_voltage': row[Bus.NOMINAL_VOLTAGE]}


def populate_utility(cur, nodes):
    try:
        cur.execute("""SELECT * FROM public.client_node, public.client_utility
                    WHERE
                    client_node.id = client_utility.node_ptr_id""")
    except:
        print("I can't SELECT from utility")

    rows = cur.fetchall()

    for row in rows:
        nodes[row[Utility.ID]] = \
            {'id': row[Utility.ID], 
             'name': row[Utility.NAME],
             'operational_status': row[Utility.OPERATIONAL_STATUS],
             'is_bus': row[Utility.IS_BUS],
             'voltage_1_magnitude': row[Utility.VOLTAGE_1_MAGNITUDE],
             'voltage_1_angle': row[Utility.VOLTAGE_1_ANGLE],
             'voltage_1_pu': row[Utility.VOLTAGE_1_PU],
             'type': row[Utility.TYPE],
             'latitude': row[Utility.LATITUDE],
             'longitude': row[Utility.LONGITUDE],
             'stiffness': row[Utility.STIFFNESS],
             'base_power': row[Utility.BASE_POWER],
             'LL_voltage': row[Utility.LL_VOLTAGE],
             'nominal_voltage': row[Bus.NOMINAL_VOLTAGE],
             'voltage_angle': row[Utility.VOLTAGE_ANGLE],
             'short_circuit_3_phase': row[Utility.SHORT_CIRCUIT_3_PHASE],
             'short_circuit_SLG': row[Utility.SHORT_CIRCUIT_SLG],
             'r_1': row[Utility.R_1],
             'x_1': row[Utility.X_1],
             'r_0': row[Utility.R_0],
             'x_0': row[Utility.X_0],
             'current_1_magnitude': row[Utility.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[Utility.CURRENT_1_ANGLE]}


def populate_transformer(cur, connections):
    try:
        cur.execute("""SELECT * FROM public.client_connection, public.client_twowindingtransformer
                    WHERE
                    client_connection.id = client_twowindingtransformer.connection_ptr_id""")
    except:
        print("I can't SELECT from utility")

    rows = cur.fetchall()

    for row in rows:
        connections[row[TwoWindingTransformer.ID]] = \
            {'id': row[TwoWindingTransformer.ID], 
             'name': row[TwoWindingTransformer.NAME],
             'operational_status': row[TwoWindingTransformer.OPERATIONAL_STATUS],
             'real_power_entering': row[TwoWindingTransformer.REAL_POWER_ENTERING],
             'real_power_leaving': row[TwoWindingTransformer.REAL_POWER_LEAVING],
             'reactive_power_entering': row[TwoWindingTransformer.REACTIVE_POWER_ENTERING],
             'reactive_power_leaving': row[TwoWindingTransformer.REACTIVE_POWER_LEAVING],
             'type': row[TwoWindingTransformer.TYPE],
             'from_bus': row[TwoWindingTransformer.FROM_BUS],
             'to_bus': row[TwoWindingTransformer.TO_BUS],
             'from_bus_voltage_rating': row[TwoWindingTransformer.FROM_BUS_VOLTAGE_RATING],
             'to_bus_voltage_rating': row[TwoWindingTransformer.TO_BUS_VOLTAGE_RATING],
             'from_bus_wiring': row[TwoWindingTransformer.FROM_BUS_WIRING],
             'to_bus_wiring': row[TwoWindingTransformer.TO_BUS_WIRING],
             'power_rating': row[TwoWindingTransformer.POWER_RATING],
             'x_percent': row[TwoWindingTransformer.X_PERCENT],
             'r_percent': row[TwoWindingTransformer.R_PERCENT],
             'tap_percent': row[TwoWindingTransformer.TAP_PERCENT],
             'tap_side': row[TwoWindingTransformer.TAP_SIDE],
             'min_tap': row[TwoWindingTransformer.MIN_TAP],
             'current_1_magnitude': row[TwoWindingTransformer.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[TwoWindingTransformer.CURRENT_1_ANGLE],
             'max_tap': row[TwoWindingTransformer.MAX_TAP]}


def populate_direct(cur, connections):
    try:
        cur.execute("""SELECT * FROM public.client_connection, public.client_directconnection
                    WHERE
                    client_connection.id = client_directconnection.connection_ptr_id""")
    except:
        print("I can't SELECT from utility")

    rows = cur.fetchall()

    for row in rows:
        connections[row[DirectConnection.ID]] = \
            {'id': row[DirectConnection.ID],
             'name': row[DirectConnection.NAME],
             'operational_status': row[DirectConnection.OPERATIONAL_STATUS],
             'real_power_entering': row[DirectConnection.REAL_POWER_ENTERING],
             'real_power_leaving': row[DirectConnection.REAL_POWER_LEAVING],
             'reactive_power_entering': row[DirectConnection.REACTIVE_POWER_ENTERING],
             'reactive_power_leaving': row[DirectConnection.REACTIVE_POWER_LEAVING],
             'type': row[DirectConnection.TYPE],
             'from_bus': row[DirectConnection.FROM_BUS],
             'to_bus': row[DirectConnection.TO_BUS],
             'from_bus_voltage_rating': row[DirectConnection.FROM_BUS_VOLTAGE_RATING],
             'to_bus_voltage_rating': row[DirectConnection.TO_BUS_VOLTAGE_RATING],
             'current_1_magnitude': row[DirectConnection.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[DirectConnection.CURRENT_1_ANGLE]}


def populate_cables(cur, connections):
    try:
        cur.execute("""SELECT * FROM public.client_connection, public.client_cable
                    WHERE
                    client_connection.id = client_cable.connection_ptr_id""")
    except:
        print("I can't SELECT from utility")

    rows = cur.fetchall()

    for row in rows:
        connections[row[Cable.ID]] = \
            {'id': row[Cable.ID],
             'name': row[Cable.NAME],
             'operational_status': row[Cable.OPERATIONAL_STATUS],
             'real_power_entering': row[Cable.REAL_POWER_ENTERING],
             'real_power_leaving': row[Cable.REAL_POWER_LEAVING],
             'reactive_power_entering': row[Cable.REACTIVE_POWER_ENTERING],
             'reactive_power_leaving': row[Cable.REACTIVE_POWER_LEAVING],
             'type': row[Cable.TYPE],
             'from_bus': row[Cable.FROM_BUS],
             'to_bus': row[Cable.TO_BUS],
             'linecode_object_id': row[Cable.LINECODE_OBJECT_ID],
             'voltage_rating': row[Cable.VOLTAGE_RATING],
             'length': row[Cable.LENGTH],
             'number_of_cables': row[Cable.NUMBER_OF_CABLES],
             'current_1_magnitude': row[Cable.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[Cable.CURRENT_1_ANGLE]}


def populate_overhead(cur, connections):
    try:
        cur.execute("""SELECT * FROM public.client_connection, public.client_overheadline
                    WHERE
                    client_connection.id = client_overheadline.connection_ptr_id""")
    except:
        print("I can't SELECT from utility")

    rows = cur.fetchall()

    for row in rows:
        connections[row[OverheadLine.ID]] = \
            {'id': row[OverheadLine.ID],
             'name': row[OverheadLine.NAME],
             'operational_status': row[OverheadLine.OPERATIONAL_STATUS],
             'real_power_entering': row[OverheadLine.REAL_POWER_ENTERING],
             'real_power_leaving': row[OverheadLine.REAL_POWER_LEAVING],
             'reactive_power_entering': row[OverheadLine.REACTIVE_POWER_ENTERING],
             'reactive_power_leaving': row[OverheadLine.REACTIVE_POWER_LEAVING],
             'type': row[OverheadLine.TYPE],
             'from_bus': row[OverheadLine.FROM_BUS],
             'to_bus': row[OverheadLine.TO_BUS],
             'wiredata_object_id': row[OverheadLine.WIREDATA_OBJECT_ID],
             'number_of_conductors': row[OverheadLine.NUMBER_OF_CONDUCTORS],
             'length': row[OverheadLine.LENGTH],
             'soil_resistivity': row[OverheadLine.SOIL_RESISTIVITY],
             'current_1_magnitude': row[OverheadLine.CURRENT_1_MAGNITUDE],
             'current_1_angle': row[OverheadLine.CURRENT_1_ANGLE],
             'x_1': row[OverheadLine.X_1],
             'x_2': row[OverheadLine.X_2],
             'x_3': row[OverheadLine.X_3],
             'x_4': row[OverheadLine.X_3],
             'y_1': row[OverheadLine.Y_1],
             'y_2': row[OverheadLine.Y_2],
             'y_3': row[OverheadLine.Y_3],
             'y_4': row[OverheadLine.Y_4],
             'h_1': row[OverheadLine.H_1],
             'h_2': row[OverheadLine.H_2],
             'h_3': row[OverheadLine.H_3],
             'h_4': row[OverheadLine.H_4],
             'nominal_LL_voltage': row[OverheadLine.NOMINAL_LL_VOLTAGE]}


def populate_wire_data(cur, wire_data):
    try:
        cur.execute("""SELECT * FROM public.client_wiredata""")
    except:
        print("I can't SELECT from wiredata")

    rows = cur.fetchall()

    for row in rows:
        wire_data[row[WireData.ID]] = \
            {'id': row[WireData.ID],
             'name': row[WireData.NAME],
             'resistance_50_C': row[WireData.RESISTANCE_50_C],
             'continuous_ampacity': row[WireData.CONTINUOUS_AMPACITY],
             'emergency_ampacity': row[WireData.EMERGENCY_AMPACITY],
             'diameter': row[WireData.DIAMETER],
             'GMR': row[WireData.GMR],
             'type': row[WireData.TYPE],
             'wire_type': row[WireData.WIRE_TYPE]}


def populate_line_code(cur, line_code):
    try:
        cur.execute("""SELECT * FROM public.client_linecode""")
    except:
        print("I can't SELECT from linecode")

    rows = cur.fetchall()

    for row in rows:
        line_code[row[LineCode.ID]] = \
            {'id': row[LineCode.ID],
             'name': row[LineCode.NAME],
             'r_1': row[LineCode.R_1],
             'x_1': row[LineCode.X_1],
             'r_0': row[LineCode.R_0],
             'x_0': row[LineCode.X_0],
             'continuous_ampacity': row[LineCode.CONTINUOUS_AMPACITY],
             'emergency_ampacity': row[LineCode.EMERGENCY_AMPACITY]}

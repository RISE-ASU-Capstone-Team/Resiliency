from powercalc.PowerMethods import *
from powercalc.PowerClasses import *
from os import environ
import subprocess
import powercalc.Psycopg as Psycopg
from powercalc.Constants import *
import csv
import psycopg2
import time

# Simulation process
# 1. Begin Simulation (Loop with start/pause functionality)
# 2. Read power components from Database
# 3. Create python objects from [2] ----- Seen below
# 4. Write OpenDSS file using [3] ----- Seen below
# 5. Run OpenDSS simulation ----- Seen below
# 6. Read OpenDSS outputs (currents, voltages, power) ----- TBD
# 7. Write outputs to Database from [6]
# 8. Return to step [2]


def main():
    # There has to be exactly one swing bus.
    # It can either be a utility or a synchronous generator.
    # Here I'm setting the swing bus to utility with object ID number 1

    '''
    # LineCode
    linecodenew1 = LineCode(1, 'linecode1', True, 500.0,
                            700.0, 2.0, 5.0, 2.5,
                            6.0)
    p_list_linecode.append(linecodenew1)

    # WireData
    wiredatanew1 = WireData(1, 'wiredata1', True, 9.0,
                            2.5, 300.0, 400.0, 10.0,
                            10.0, 3.0, 200.0, 300.0,
                            8.0)
    p_list_wiredata.append(wiredatanew1)

    # POWER_NODE
    # Utility
    utilitynew1 = Utility(1, 'utility1', True, 100.0,
                          100.0, 13.8, 100.0, 0.0,
                          100.0, 100.0, False, 1.5,
                          2.0, 5.5, 6.5)
    p_list_utility.append(utilitynew1)
    utilitynew2 = Utility(2, 'utility2', True, 100.0,
                          100.0, 13.8, 100.0, 0.0,
                          100.0, 100.0, False, 1.5,
                          2.0, 5.5, 6.5)
    p_list_utility.append(utilitynew2)

    # SynchGenerator
    synchgennew1 = SynchGenerator(1, 'syncgen1', True, 200.0,
                                  200.0, 13.8, True, 100.0,
                                  1800, 4, 85.0, 2)
    p_list_synchgenerator.append(synchgennew1)

    # Load
    loadnew1 = Load(1, 'load1', True, 300.0,
                    300.0, 1.2, 2, 90.0,
                    1, 0.9, 2, 1)
    p_list_load.append(loadnew1)

    # Bus
    busnew1 = Bus(1, 'bus1', True, 400.0,
                  400.0, 13.8)
    p_list_bus.append(busnew1)

    # POWER_ARC
    # OverheadLine
    overheadlinenew1 = OverheadLine(1, 'overheadline1', True, 1,
                                    UTILITY_ID, 1, BUS_ID, 1,
                                    4, -1.0, 2.0, 3.5,
                                    10.0, 10.0, 10.0, 100.0,
                                    100.0, True, 3.5, 5.0)
    p_list_line.append(overheadlinenew1)

    # Cable
    cablenew1 = Cable(1, 'cable1', True, 2,
                      UTILITY_ID, 1, BUS_ID, 1,
                      100.0, 50.0, 1)
    p_list_cable.append(cablenew1)

    # DirectConnection
    connectnew1 = DirectConnection(1, 'directconnect1', True, 1,
                                   SYNCHGENERATOR_ID, 1, BUS_ID)
    p_list_directconnection.append(connectnew1)

    # TwoWindingTransformer
    transfnew1 = TwoWindingTransformer(1, 'twtrans1', True, 1,
                                       UTILITY_ID, 1, BUS_ID, 13.8,
                                       13.8, 2, 2, 100,
                                       6.8, 2.1, 100.0, 32,
                                       False, 0.9, 1.1)
    p_list_transformer.append(transfnew1)
    transfnew2 = TwoWindingTransformer(2, 'twtrans2', True, 1,
                                       BUS_ID, 1, LOAD_ID, 13.8,
                                       1.2, 2, 2, 90,
                                       7.0, 2.2, 100.0, 32,
                                       False, 0.9, 1.1)
    p_list_transformer.append(transfnew2)

    # UNCOMMENT THESE LINES TO GET HELP WITH CLASS DECLARATIONS
    # Utility.helpclass()
    # SynchGenerator.helpclass()
    # Load.helpclass()
    # Bus.helpclass()

    # LineCode.helpclass()
    # WireData.helpclass()

    # OverheadLine.helpclass()
    # Cable.helpclass()
    # DirectConnection.helpclass()
    # TwoWindingTransformer.helpclass()
    '''

    nodes, connections, wire_data, line_codes = Psycopg.populate_components()
    circuit_found = False
    p_temp = []

    with open('riseout.dss', 'w') as fileout:
        fileout.write('Clear\nSet DefaultBaseFrequency=60\n')
        fileout.write('\n// Source bus\n')
        fileout.write('\n// Voltage sources\n')
        fileout.write('\n// Generators (synchronous, solar, wind)\n')
        fileout.write('// RPM is unused\n')
        for key in nodes:
            if nodes[key]['type'] == Power.UTILITY:
                if not circuit_found:
                    p_write_circuit(fileout, nodes[key])
                    PowerNode.swing_component_ID_number = key
                    circuit_found = True
                    p_temp.append(str(nodes[key]['nominal_voltage']))
                else:
                    p_write_v_source(fileout, nodes[key])
                    p_temp.append(str(nodes[key]['nominal_voltage']))
            elif nodes[key]['type'] == Power.SYNCHRONOUS_GENERATOR:
                p_write_sync_generator(fileout, nodes[key])
            elif nodes[key]['type'] == Power.LOAD:
                p_write_load(fileout, nodes[key])

        p_write_pv(fileout, p_list_pv)
        p_write_wind(fileout, p_list_wind)
        fileout.write('\n// Wire Data\n')

        for key in wire_data:
            p_write_wire_data(fileout, wire_data[key])

        for key in line_codes:
            p_write_line_code(fileout, line_codes[key])

        fileout.write('\n// Overhead Lines\n')
        fileout.write('\n// Line Codes\n')
        fileout.write('\n// Cables, ATS and Connections\n')
        fileout.write('\n// Transformers\n')
        fileout.write('\n// Voltage bases\n')
        for key in connections:
            if connections[key]['type'] == Power.OVERHEAD_LINE:
                p_write_line(fileout, connections[key],
                             wire_data[connections[key]['wiredata_object_id']],
                             # ----------- TODO: CHANGE THIS -----------------------------------
                             wire_data[2],
                             nodes[connections[key]['from_bus']],
                             nodes[connections[key]['to_bus']])
            elif connections[key]['type'] == Power.CABLE:
                p_write_cable(fileout, connections[key],
                             line_codes[connections[key]['linecode_object_id']],
                             nodes[connections[key]['from_bus']],
                             nodes[connections[key]['to_bus']])
            elif connections[key]['type'] == Power.DIRECT_CONNECTION:
                p_write_direct_connection(fileout, connections[key],
                             nodes[connections[key]['from_bus']],
                             nodes[connections[key]['to_bus']])
            elif connections[key]['type'] == Power.TWO_WINDING_TRANSFORMER:
                p_write_transformer(fileout, connections[key],
                             nodes[connections[key]['from_bus']],
                             nodes[connections[key]['to_bus']])
                p_temp.append(str(connections[key]['from_bus_voltage_rating']))
                p_temp.append(str(connections[key]['to_bus_voltage_rating']))

        p_write_voltage_bases(fileout, p_temp)

        fileout.write(
            '\n// Solve study\nSolve BaseFrequency={!s} MaxIter={!s}\n'
            ''.format(base_frequency, opendss_iter))

        fileout.write(
            '\n// Export results\nExport Summary (summary.csv)\n'
            'Export Voltages (voltages.csv)\nExport Currents (currents.csv)\n'
            'Export Overloads (overloads.csv)\n'
            'Export Powers KVA (powers.csv)\n')
        fileout.close()

    if not circuit_found:
        print('No calc-ability without a utility silly.')
    else:
        environ['PATH'] += ';e:\\Program Files\\OpenDSS\\x64'
        subprocess.run('OpenDSS riseout.dss -nogui', shell=True)
        done = False
        start = time.time()
        step = time.time()
        while not done:
            try:
                with open('currents.csv', 'r') as file_in:
                    done = True
                    file_in.close()
                read_currents(nodes, connections)
                read_powers(nodes, connections)
                read_voltages(nodes)
                update_database(nodes, connections)
            except:
                if time.time() - start > 5:
                    done = True
                if time.time() - step > 1:
                    print('calculating...')
                    step = time.time()


def read_currents(nodes, connections):
    with open('currents.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        for row in reader:
            cat = row[0].split('.')[0]
            if cat != OpenDSS.ELEMENT and len(row) > 5:
                com_info = row[0].split('.')[1].split('_')
                if com_info[0] != OpenDSS.SOURCE and len(cat) > 3:
                    if cat == OpenDSS.VSOURCE or cat == OpenDSS.LOAD \
                            or cat == OpenDSS.GENERATOR:
                        node_id = int(com_info[0])
                        nodes[node_id]['current_1_magnitude'] = \
                            float(row[OpenDSS.CURRENT_1_MAGNITUDE])
                        nodes[node_id]['current_1_angle'] = \
                            float(row[OpenDSS.CURRENT_1_ANGLE])
                    else:
                        con_id = int(com_info[0])
                        connections[con_id]['current_1_magnitude'] = \
                            float(row[OpenDSS.CURRENT_1_MAGNITUDE])
                        connections[con_id]['current_1_angle'] = \
                            float(row[OpenDSS.CURRENT_1_ANGLE])


def read_powers(nodes, connections):
    with open('powers.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        second = False
        for row in reader:
            cat = row[0].split('.')[0]
            if cat != OpenDSS.ELEMENT and len(row) > 3:
                com_info = row[0].split('.')[1].split('_')
                if cat == OpenDSS.LOAD or cat == OpenDSS.GENERATOR:
                    node_id = int(com_info[0])
                    nodes[node_id]['real_power'] = \
                        float(row[OpenDSS.REAL_POWER])
                    nodes[node_id]['reactive_power'] = \
                        float(row[OpenDSS.REACTIVE_POWER])
                else:
                    if not second:
                        con_id = int(com_info[0])
                        connections[con_id]['real_power_entering'] = \
                            float(row[OpenDSS.REAL_POWER])
                        connections[con_id]['reactive_power_entering'] = \
                            float(row[OpenDSS.REACTIVE_POWER])
                        second = True
                    else:
                        con_id = int(com_info[0])
                        connections[con_id]['real_power_leaving'] = \
                            float(row[OpenDSS.REAL_POWER])
                        connections[con_id]['reactive_power_leaving'] = \
                            float(row[OpenDSS.REACTIVE_POWER])
                        second = False


def read_voltages(nodes):
    with open('voltages.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        for row in reader:
            if len(row) > 5:
                com_info = row[0].split('_')
                if com_info[0] != OpenDSS.SOURCEBUS \
                        and com_info[0] != OpenDSS.BUS:
                    node_id = int(com_info[0])
                    nodes[node_id]['voltage_1_magnitude'] = \
                        float(row[OpenDSS.VOLTAGE_1_MAGNITUDE])
                    nodes[node_id]['voltage_1_angle'] = \
                        float(row[OpenDSS.VOLTAGE_1_ANGLE])
                    nodes[node_id]['voltage_1_PU'] = \
                        float(row[OpenDSS.VOLTAGE_1_PU])


def update_database(nodes, connections):
    try:
        conn = psycopg2.connect("dbname='" + Database.NAME + "' user='" +
                                Database.USER + "' host='" + Database.HOST +
                                "' port='" + Database.PORT + "' password='" +
                                Database.PASSWORD + "'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()

    for key in nodes:
        node = nodes[key]
        node_id = str(node['id'])
        val_str = set_node(node)
        query = 'update ' + Tables.NODE + ' SET ' + val_str + \
                ' where id = ' + node_id
        cur.execute(query)
        conn.commit()
        if node['type'] != Power.BUS:
            val_str = 'current_1_magnitude=' + str(node['current_1_magnitude'])
            val_str += ',current_1_angle=' + str(node['current_1_angle'])
            if node['type'] != Power.UTILITY:
                val_str += ',real_power=' + str(node['real_power'])
                val_str += ',reactive_power=' + str(node['reactive_power'])
            query = 'update ' + comp_type_eval(node['type'], is_node=True) + \
                    " SET " + val_str + ' where node_ptr_id = ' + node_id
            cur.execute(query)
            conn.commit()

    for key in connections:
        con = connections[key]
        con_id = str(con['id'])
        val_str = set_connection(con)
        query = 'update ' + Tables.CONNECTION + ' SET ' + val_str + \
                ' where id = ' + con_id
        cur.execute(query)
        conn.commit()

    cur.execute('update client_dbchanges set update_check=' +
                str(time.time())+' where id = 1')
    conn.commit()
    conn.close()


def set_node(node):
    val_str = 'voltage_1_magnitude=' + str(node['voltage_1_magnitude'])
    val_str += ',voltage_1_angle=' + str(node['voltage_1_angle'])
    val_str += ',"voltage_1_PU"='
    val_str += str(node['voltage_1_PU'])
    return val_str


def set_connection(con):
    val_str = 'current_1_magnitude=' + str(con['current_1_magnitude'])
    val_str += ',current_1_angle=' + str(con['current_1_angle'])
    val_str += ',real_power_entering=' + str(con['real_power_entering'])
    val_str += ',reactive_power_entering=' + str(con['reactive_power_entering'])
    val_str += ',real_power_leaving=' + str(con['real_power_leaving'])
    val_str += ',reactive_power_leaving=' + str(con['reactive_power_leaving'])
    return val_str


if __name__ == '__main__':
    main()

    # THIS CODE RUNS OPENDSS SIMULATIONS USING COMMAND PROMPT
    # from os import environ
    # import subprocess
    ##
    # def main():
    #    environ['PATH'] += ';e:\\Program Files\\OpenDSS\\x64'
    #    subprocess.run('OpenDSS simulation.dss -nogui', shell=True)

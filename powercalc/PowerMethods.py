from powercalc.PowerClasses import *
from powercalc.Constants import *
import math

p_templist = []

switchConvertWiringToStr = {
    # delta 1.2.3
    0: 'delta',
    # wye ungrounded 1.2.3.4 with Rneut=-1
    1: 'wye',
    # wye solidly 1.2.3.0
    2: 'wye',
    # wye impedance 1.2.3.4 with Rneut=r and Xneut=x
    3: 'wye'
}

switchConvertWiringToNum = {
    # delta 1.2.3
    0: '1.2.3',
    # wye ungrounded 1.2.3.4 with Rneut=-1
    1: '1.2.3.4',
    # wye solidly 1.2.3.0
    2: '1.2.3.0',
    # wye impedance 1.2.3.4 with Rneut=r and Xneut=x
    3: '1.2.3.4'
}

switchConvertWiringToNeut = {
    # delta 1.2.3
    0: '',
    # wye ungrounded 1.2.3.4 with Rneut=-1
    1: 'Rneut=-1',
    # wye solidly 1.2.3.0
    2: '',
    # wye impedance 1.2.3.4 with Rneut=r and Xneut=x
    3: '1.2.3.4'
}

switchListReturnObject = {
    TWOWINDINGTRANSFORMER_ID: p_list_transformer,
    CABLE_ID: p_list_cable,
    DIRECTCONNECTION_ID: p_list_directconnection,
    OVERHEADLINE_ID: p_list_line,
    BUS_ID: p_list_bus,
    LOAD_ID: p_list_load,
    SYNCHGENERATOR_ID: p_list_synchgenerator,
    UTILITY_ID: p_list_utility,
    WIREDATA_ID: p_list_wiredata,
    LINECODE_ID: p_list_linecode
}


def p_helpclass():
    def allPowerArcs():
        return PowerArc.__subclasses__()

    def allPowerNodes():
        return PowerNode.__subclasses__()

    print('CLASS NAME')
    print('------------')
    for arc in allPowerArcs():
        print(arc.__name__)
    for node in allPowerNodes():
        print(node.__name__)
    print('')


def p_convert_wiring_to_str(wiring_in):
    return switchConvertWiringToStr.get(wiring_in, 'wye')


def p_convert_wiring_to_num(wiring_in):
    return switchConvertWiringToNum.get(wiring_in, '.1.2.3.0')


def p_convert_wiring_to_neut(wiring_in):
    return switchConvertWiringToNeut.get(wiring_in, '')


def p_list_return_object(COMPONENT_ID, object_ID):
    return switchListReturnObject.get(COMPONENT_ID, '')[object_ID - 1]


def p_write_circuit(fileout, node):
    try:
        fileout.write(
            'New \'Circuit.{!s}\' basekv=\'{!s}\' pu=\'{!s}\' Angle=\'{!s}\' '
            'Phases=\'{!s}\' Mvasc3=\'{!s}\' Mvasc1=\'{!s}\' R1=\'{!s}\' X1=\''
            '{!s}\' R0=\'{!s}\' X0=\'{!s}\'\n'.format(
                str(node['id']) + '_' + str(node['type']) + '_' +
                str(node['name']),
                str(node['nominal_voltage']), DEFAULTPU,
                str(node['voltage_angle']), DEFAULTPHASES,
                str(node['short_circuit_3_phase']),
                str(node['short_circuit_SLG']),
                str(node['r_1']), str(node['x_1']),
                str(node['r_0']), str(node['x_0'])))
    except:
        print('Error writing circuit ' + str(node['id']))
        pass


def p_write_v_source(fileout, node):
    try:
        fileout.write(
            'New \'Vsource.{!s}\' bus1=\'{!s}.1.2.3.0\' basekv=\''
            '{!s}\' pu=\'{!s}\' Angle=\'{!s}\' Phases=\'{!s}\' '
            'Mvasc3=\'{!s}\' Mvasc1=\'{!s}\' R1=\'{!s}\' X1=\''
            '{!s}\' R0=\'{!s}\' X0=\'{!s}\'\n'.format(
                str(node['id']) + '_' + str(node['type']) + '_' +
                str(node['name']),
                str(node['id']) + '_' + str(node['type']) + '_' +
                str(node['name']),
                str(node['nominal_voltage']), DEFAULTPU,
                str(node['voltage_angle']), DEFAULTPHASES,
                str(node['short_circuit_3_phase']),
                str(node['short_circuit_SLG']),
                str(node['r_1']), str(node['x_1']),
                str(node['r_0']), str(node['x_0'])))
    except:
        print('Error writing v source ' + str(node['id']))
        pass


def p_write_sync_generator(fileout, node):
    try:
        fileout.write(
            'New \'Generator.{!s}\' bus1=\'{!s}.{!s}\' Phases=\''
            '{!s}\' Kv=\'{!s}\' Kw =\'{!s}\' Pf=\'{!s}\' Model=\''
            '{!s}\' Conn=\'{!s}\'\n'.format(
                str(node['id']) + '_' + str(node['type']) + '_' +
                str(node['name']),
                str(node['id']) + '_' + str(node['type']) + '_' +
                str(node['name']), p_convert_wiring_to_num(node['wiring']),
                DEFAULTPHASES, str(node['nominal_voltage']),
                str(node['power_rating']), str(node['power_factor_percent'] * 0.01),
                '1', p_convert_wiring_to_str(node['wiring'])))
    except ValueError as e:
        print(e.__traceback__)
        print('Error writing sync gen ' + str(node['id']))
        pass


def p_write_pv(fileout, list):
    pass


def p_write_wind(fileout, list):
    pass


def p_write_load(fileout, node):
        try:
            fileout.write(
                'New \'Load.{!s}\' bus1=\'{!s}.{!s}\' Phases=\'{!s}\' Kv=\''
                '{!s}\' PF=\'{!s}\' Model=\'{!s}\' Conn=\'{!s}\' Rneut=\''
                '{!s}\' Xneut=\'{!s}\' Vminpu=\'{!s}\' kVA=\'{!s}\'\n'.format(
                    str(node['id']) + '_' + str(node['type']) + '_' +
                    str(node['name']),
                    str(node['id']) + '_' + str(node['type']) + '_' +
                    str(node['name']), p_convert_wiring_to_num(node['wiring']),
                    DEFAULTPHASES, str(node['nominal_voltage']),
                    str(node['power_factor_percent'] * 0.01 * node['power_factor_type']),
                    str(node['load_model']),
                    p_convert_wiring_to_str(node['wiring']), '0',
                    '0', str(node['min_pu_voltage']),
                    str(node['power_rating'])))
        except ValueError as e:
            print(e.__traceback__)
            print('Error writing load ' + str(node['id']))
            pass


def p_write_wire_data(fileout, data):
    try:
        if data['wire_type'] == Power.PHASE:
            p_temp = 'New \'WireData.WD_phase_{!s}\' Rac=\'{!s}\' ' \
                     'Runits=\'{!s}\' GMRac=\'{!s}\' GMRunits=\'{!s}\' ' \
                     'Radunits=\'{!s}\' Normamps=\'{!s}\' Emergamps=\'' \
                     '{!s}\' Diam=\'{!s}\'\n'.format(
                        str(data['id']) + '_' + str(data['wire_type']) +
                        '_' + str(data['name']),
                        str(data['resistance_50_C']),
                        'kft', str(data['GMR']), 'ft',
                        'in', str(data['continuous_ampacity']),
                        str(data['emergency_ampacity']),
                        str(data['diameter']))
        else:
            p_temp = 'New \'WireData.WD_neut_{!s}\' ' \
                      'Rac=\'{!s}\' Runits=\'{!s}\' ' \
                      'GMRac=\'{!s}\' GMRunits=\'' \
                      '{!s}\' Radunits=\'{!s}\' ' \
                      'Normamps=\'{!s}\' Emergamps=\'' \
                      '{!s}\' Diam=\'{!s}\'\n'.format(
                          str(data['id']) + '_' + str(data['wire_type']) +
                          '_' + str(data['name']),
                          str(data['resistance_50_C']),
                          'kft', str(data['GMR']), 'ft',
                          'in', str(data['continuous_ampacity']),
                          str(data['emergency_ampacity']),
                          str(data['diameter']))
        fileout.write(p_temp)
    except:
        print('Error writing wire_data ' + str(data['id']))
        pass


def p_write_line(fileout, con, wire, wire2, bus1, bus2):
    try:

        p_temp = 'New \'LineGeometry.LG_{!s}\' Nconds=\'' \
                 '{!s}\' Nphases=\'{!s}\'\n'.format(
                    str(con['id']) + '_' + str(con['type']) +
                    '_' + str(con['name']),
                    con['number_of_conductors'], DEFAULTPHASES)
        p_temp += '~ Cond=1 Wire=\'WD_phase_{!s}\' X=\'{!s}\' H=\'' \
                  '{!s}\' Units=\'{!s}\'\n'.format(
                    str(wire['id']) + '_' + str(wire['wire_type']) +
                    '_' + str(wire['name']),
                    con['x_1'], con['h_1'], 'ft')
        p_temp += '~ Cond=2 Wire=\'WD_phase_{!s}\' X=\'{!s}\' H=\'' \
                  '{!s}\' Units=\'{!s}\'\n'.format(
                    str(wire['id']) + '_' + str(wire['wire_type']) +
                    '_' + str(wire['name']),
                    con['x_2'], con['h_2'], 'ft')
        p_temp += '~ Cond=3 Wire=\'WD_phase_{!s}\' X=\'{!s}\' ' \
                  'H=\'{!s}\' Units=\'{!s}\'\n'.format(
                    str(wire['id']) + '_' + str(wire['wire_type']) +
                    '_' + str(wire['name']),
                    con['x_3'], con['h_3'], 'ft')
        if con['number_of_conductors'] == 4:
            p_temp += '~ Cond=4 Wire=\'WD_neut_{!s}\' X=\'{!s}\' ' \
                      'H=\'{!s}\' Units=\'{!s}\' reduce=\'' \
                      '{!s}\'\n'.format(
                        str(wire2['id']) + '_' + str(wire2['wire_type']) +
                        '_' + str(wire2['name']),
                        con['x_4'], con['h_4'], 'ft', 'y')
        p_temp += 'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'' \
                  '{!s}.1.2.3\' Length=\'{!s}\' Phases=\'{!s}\' ' \
                  'BaseFreq=\'{!s}\' Rho=\'{!s}\' Geometry=\'LG_' \
                  '{!s}\' Units=\'{!s}\'\n'.format(
                    str(con['id']) + '_' + str(con['type']) +
                    '_' + str(con['name']),
                    str(bus1['id']) + '_' + str(bus1['type']) + '_' +
                    str(bus1['name']),
                    str(bus2['id']) + '_' + str(bus2['type']) + '_' +
                    str(bus2['name']),
                    con['length'], DEFAULTPHASES, base_frequency,
                    con['soil_resistivity'],
                    str(con['id']) + '_' + str(con['type']) +
                    '_' + str(con['name']), 'ft')
        fileout.write(p_temp)
    except ValueError as e:
        print(e.__traceback__)
        print('Error writing line ' + str(con['id']))
        pass


def p_write_line_code(fileout, line):
    try:
        fileout.write(
            'New \'Linecode.LC_{!s}\' nphases=\'{!s}\' R1=\'{!s}\' X1=\''
            '{!s}\' R0=\'{!s}\' X0=\'{!s}\' Units=\'{!s}\' Normamps=\''
            '{!s}\' Emergamps=\'{!s}\'\n'.format(
                str(line['id']) +
                '_' + str(line['name']),
                DEFAULTPHASES, str(line['r_1']), str(line['x_1']),
                str(line['r_0']), str(line['x_0']), 'kft',
                str(line['continuous_ampacity']),
                str(line['emergency_ampacity'])))
    except:
        print('Error writing line code ' + str(line['id']))
        pass


def p_write_cable(fileout, con, line, bus1, bus2):
    try:
        fileout.write(
            'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'{!s}.1.2.3\' '
            'LineCode=\'LC_{!s}\' Length=\'{!s}\' Units=\'{!s}\'\n'.format(
                str(con['id']) + '_' + str(con['type']) +
                '_' + str(con['name']),
                str(bus1['id']) + '_' + str(bus1['type']) +
                '_' + str(bus1['name']),
                str(bus2['id']) + '_' + str(bus2['type']) +
                '_' + str(bus2['name']),
                str(line['id']) +
                '_' + str(line['name']),
                con['length'], 'ft'))
    except:
        print('Error writing cable ' + str(con['id']))
        pass


def p_write_direct_connection(fileout, con, bus1, bus2):
    try:
        fileout.write(
            'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'{!s}.1.2.3\' '
            'Phases=\'{!s}\' Switch=\'{!s}\'\n'.format(
                str(con['id']) + '_' + str(con['type']) +
                '_' + str(con['name']),
                str(bus1['id']) + '_' + str(bus1['type']) +
                '_' + str(bus1['name']),
                str(bus2['id']) + '_' + str(bus2['type']) +
                '_' + str(bus2['name']),
                DEFAULTPHASES, 'True'))
    except:
        print('Error writing direct con ' + str(con['id']))
        pass


def p_write_transformer(fileout, con, bus1, bus2):
    try:
        p_temp = 'New \'Transformer.{!s}\' Phases=\'{!s}\' ' \
                 'Windings=\'{!s}\' XHL=\'{!s}\' %LoadLoss=\'' \
                 '{!s}\'\n'.format(
                   str(con['id']) + '_' + str(con['type']) +
                   '_' + str(con['name']),
                   DEFAULTPHASES, DEFAULTWINDINGS,
                   str(con['x_percent'] * 0.01),
                   str(con['r_percent'] * 0.01))
        p_temp += '~ wdg=1 Bus=\'{!s}.{!s}\' kV=\'{!s}\' ' \
                  'kVA=\'{!s}\' Conn=\'{!s}\'\n'.format(
                    str(bus1['id']) + '_' + str(bus1['type']) +
                    '_' + str(bus1['name']),
                    p_convert_wiring_to_num(con['from_bus_wiring']),
                    con['from_bus_voltage_rating'], con['power_rating'],
                    p_convert_wiring_to_str(con['from_bus_wiring']))
        p_temp += '~ wdg=2 Bus=\'{!s}.{!s}\' kV=\'{!s}\' kVA=\'' \
                  '{!s}\' Conn=\'{!s}\'\n'.format(
                    str(bus2['id']) + '_' + str(bus2['type']) +
                    '_' + str(bus2['name']),
                    p_convert_wiring_to_num(con['to_bus_wiring']),
                    con['to_bus_voltage_rating'], con['power_rating'],
                    p_convert_wiring_to_str(con['to_bus_wiring']))

        fileout.write(p_temp)
    except:
        print('Error writing transformer ' + str(con['id']))
        pass


def p_write_voltage_bases(fileout, p_temp):
    temp_v_bases = set(p_temp)

    fileout.write('Set VoltageBases=[')

    for elem in temp_v_bases:
        fileout.write(' {!s}'.format(elem))

    temp_v_bases.clear()

    fileout.write(']\nCalcVoltageBases\n')

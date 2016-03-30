from powercalc.PowerClasses import *
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
                str(node['nominal_LL_voltage']), DEFAULTPU,
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
                str(node['nominal_LL_voltage']), DEFAULTPU,
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
        if elem.COMPONENT_ID_NUMBER is PowerNode.swing_component_ID_number \
                and elem.object_ID_number \
                is PowerNode.swing_object_ID_number:
            pass
        else:
            fileout.write(
                'New \'Generator.{!s}\' bus1=\'{!s}.{!s}\' Phases=\''
                '{!s}\' Kv=\'{!s}\' Kw =\'{!s}\' Pf=\'{!s}\' Model=\''
                '{!s}\' Conn=\'{!s}\'\n'.format(
                    elem.object_name,
                    elem.object_name, p_convert_wiring_to_num(elem.wiring),
                    DEFAULTPHASES, elem.nominal_LL_voltage,
                    elem.power_rating, elem.pf_percent * 0.01, '1',
                    p_convert_wiring_to_str(elem.wiring)))
    except:
        print('Error writing sync gen ' + str(node['id']))
        pass


def p_write_pv(fileout, list):
    pass


def p_write_wind(fileout, list):
    pass


def p_write_load(fileout, node):
    for elem in list:
        try:
            fileout.write(
                'New \'Load.{!s}\' bus1=\'{!s}.{!s}\' Phases=\'{!s}\' Kv=\''
                '{!s}\' PF=\'{!s}\' Model=\'{!s}\' Conn=\'{!s}\' Rneut=\''
                '{!s}\' Xneut=\'{!s}\' Vminpu=\'{!s}\' kVA=\'{!s}\'\n'.format(
                    elem.object_name,
                    elem.object_name, p_convert_wiring_to_num(elem.wiring),
                    DEFAULTPHASES, elem.nominal_LL_voltage,
                    0.01 * elem.pf_percent * elem.pf_type, elem.load_model,
                    p_convert_wiring_to_str(elem.wiring), 0,
                    0, elem.min_pu_voltage, elem.power_rating))
        except:
            print('Error writing load ' + str(node['id']))
            pass


def p_write_wire_data(fileout, data):
    for elem in list:
        try:
            p_temp = 'New \'WireData.WD_phase_{!s}\' Rac=\'{!s}\' ' \
                           'Runits=\'{!s}\' GMRac=\'{!s}\' GMRunits=\'{!s}\' ' \
                           'Radunits=\'{!s}\' Normamps=\'{!s}\' Emergamps=\'' \
                           '{!s}\' Diam=\'{!s}\'\n'.format(
                            elem.object_name,
                            elem.phase_resistance_50_C,
                            'kft', elem.phase_GMR, 'ft',
                            'in', elem.phase_continuous_ampacity,
                            elem.phase_emergency_ampacity, elem.phase_diameter)
            if elem.neutral_resistance_50_C and elem.neutral_diameter:
                p_temp += 'New \'WireData.WD_neut_{!s}\' ' \
                                'Rac=\'{!s}\' Runits=\'{!s}\' ' \
                                'GMRac=\'{!s}\' GMRunits=\'' \
                                '{!s}\' Radunits=\'{!s}\' ' \
                                'Normamps=\'{!s}\' Emergamps=\'' \
                                '{!s}\' Diam=\'{!s}\'\n'.format(
                                    elem.object_name,
                                    elem.neutral_resistance_50_C,
                                    'kft', elem.neutral_GMR, 'ft',
                                    'in', elem.neutral_continuous_ampacity,
                                    elem.neutral_emergency_ampacity,
                                    elem.neutral_diameter)
            fileout.write(p_temp)
        except:
            print('Error writing wire_data ' + str(data['id']))
            pass


def p_write_line(fileout, line):
    for elem in list:
        p_temp = None
        try:
            wire_name = p_list_return_object(WIREDATA_ID,
                                           elem.wiredata_object_ID).object_name
            p_temp = 'New \'LineGeometry.LG_{!s}\' Nconds=\'' \
                     '{!s}\' Nphases=\'{!s}\'\n'.format(
                            elem.object_name,
                            elem.number_of_conductors, DEFAULTPHASES)
            p_temp += '~ Cond=1 Wire=\'WD_phase_{!s}\' X=\'{!s}\' H=\'' \
                      '{!s}\' Units=\'{!s}\'\n'.format(
                                wire_name,
                                elem.x_1_coordinate, elem.h_1_coordinate, 'ft')
            p_temp += '~ Cond=2 Wire=\'WD_phase_{!s}\' X=\'{!s}\' H=\'' \
                      '{!s}\' Units=\'{!s}\'\n'.format(
                                wire_name,
                                elem.x_2_coordinate, elem.h_2_coordinate, 'ft')
            p_temp += '~ Cond=3 Wire=\'WD_phase_{!s}\' X=\'{!s}\' ' \
                      'H=\'{!s}\' Units=\'{!s}\'\n'.format(
                                wire_name,
                                elem.x_3_coordinate, elem.h_3_coordinate, 'ft')
            if elem.number_of_conductors == 4:
                p_temp += '~ Cond=4 Wire=\'WD_neut_{!s}\' X=\'{!s}\' ' \
                          'H=\'{!s}\' Units=\'{!s}\' reduce=\'' \
                          '{!s}\'\n'.format(
                                wire_name,
                                elem.x_4_coordinate, elem.h_4_coordinate,
                                'ft', 'y')
            p_temp += 'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'' \
                      '{!s}.1.2.3\' Length=\'{!s}\' Phases=\'{!s}\' ' \
                      'BaseFreq=\'{!s}\' Rho=\'{!s}\' Geometry=\'LG_' \
                      '{!s}\' Units=\'{!s}\'\n'.format(
                                elem.object_name,
                                p_list_return_object(elem.from_bus_component_ID,
                                                     elem.from_bus_object_ID).
                                object_name,
                                p_list_return_object(elem.to_bus_component_ID,
                                                     elem.to_bus_object_ID).
                                object_name,
                                elem.length, DEFAULTPHASES, base_frequency,
                                elem.soil_resistivity,
                                elem.object_name, 'ft')
            fileout.write(p_temp)
        except:
            print('Error writing line ' + str(line['id']))
            pass


def p_write_line_code(fileout, list):
    for elem in list:
        try:
            fileout.write(
                'New \'Linecode.LC_{!s}\' nphases=\'{!s}\' R1=\'{!s}\' X1=\''
                '{!s}\' R0=\'{!s}\' X0=\'{!s}\' Units=\'{!s}\' Normamps=\''
                '{!s}\' Emergamps=\'{!s}\'\n'.format(
                    elem.object_name,
                    DEFAULTPHASES, elem.r_1, elem.x_1, elem.r_0,
                    elem.x_0, 'kft', elem.continuous_ampacity,
                    elem.emergency_ampacity))
        except:
            print('Error writing line code ' + str(line['id']))
            pass


def p_write_cable(fileout, list):
    for elem in list:
        try:
            fileout.write(
                'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'{!s}.1.2.3\' '
                'LineCode=\'LC_{!s}\' Length=\'{!s}\' Units=\'{!s}\'\n'.format(
                    elem.object_name,
                    p_list_return_object(elem.from_bus_component_ID,
                                         elem.from_bus_object_ID).
                    object_name,
                    p_list_return_object(elem.to_bus_component_ID,
                                       elem.to_bus_object_ID).object_name,
                    p_list_return_object(LINECODE_ID,
                                         elem.linecode_object_ID).object_name,
                    elem.length, 'ft'))
        except:
            print('Error writing cable ' + str(line['id']))
            pass


def p_write_direct_connection(fileout, list):
    for elem in list:
        try:
            fileout.write(
                'New \'Line.{!s}\' Bus1=\'{!s}.1.2.3\' Bus2=\'{!s}.1.2.3\' '
                'Phases=\'{!s}\' Switch=\'{!s}\'\n'.format(
                    elem.object_name,
                    p_list_return_object(elem.from_bus_component_ID,
                                       elem.from_bus_object_ID).object_name,
                    p_list_return_object(elem.to_bus_component_ID,
                                       elem.to_bus_object_ID).object_name,
                    DEFAULTPHASES, 'True'))
        except:
            print('Error writing direct con ' + str(line['id']))
            pass


def p_write_transformer(fileout, trans_list):
    for elem in trans_list:
        p_temp = None
        try:
            p_temp = 'New \'Transformer.{!s}\' Phases=\'{!s}\' ' \
                           'Windings=\'{!s}\' XHL=\'{!s}\' %LoadLoss=\'' \
                           '{!s}\'\n'.format(
                            elem.object_name,
                            DEFAULTPHASES, DEFAULTWINDINGS,
                            elem.x_percent * 0.01,
                            elem.r_percent * 0.01)
            try:
                p_temp += '~ wdg=1 Bus=\'{!s}.{!s}\' kV=\'{!s}\' ' \
                          'kVA=\'{!s}\' Conn=\'{!s}\'\n'.format(
                            p_list_return_object(elem.from_bus_component_ID,
                                                 elem.from_bus_object_ID).
                            object_name,
                            p_convert_wiring_to_num(elem.from_bus_wiring),
                            elem.from_bus_voltage_rating, elem.power_rating,
                            p_convert_wiring_to_str(elem.from_bus_wiring))
                p_temp += '~ wdg=2 Bus=\'{!s}.{!s}\' kV=\'{!s}\' kVA=\'' \
                          '{!s}\' Conn=\'{!s}\'\n'.format(
                            p_list_return_object(elem.to_bus_component_ID,
                                                 elem.to_bus_object_ID).
                            object_name,
                            p_convert_wiring_to_num(elem.to_bus_wiring),
                            elem.to_bus_voltage_rating, elem.power_rating,
                            p_convert_wiring_to_str(elem.to_bus_wiring))
            except:
                print(
                    'ERROR: Cannot find from_bus or to_bus for '
                    'transformer {!s} node'.format(
                        elem.object_name))
            fileout.write(p_temp)
        except:
            print('Error writing transformer ' + str(line['id']))
            pass


def p_write_voltage_bases(fileout, list1, list2):
    p_temp = []

    try:
        for elem in list1:
            p_temp.append(str(elem.from_bus_voltage_rating))
            p_temp.append(str(elem.to_bus_voltage_rating))
    except:
        pass

    try:
        for elem in list2:
            p_temp.append(str(elem.nominal_LL_voltage))
    except:
        pass

    temp_v_bases = set(p_temp)
    p_temp = []

    fileout.write('Set VoltageBases=[')

    for elem in temp_v_bases:
        fileout.write(' {!s}'.format(elem))

    temp_v_bases.clear()

    fileout.write(']\nCalcVoltageBases\n')

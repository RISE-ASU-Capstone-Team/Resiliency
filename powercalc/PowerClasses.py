from powercalc.PowerGlobal import *
import abc

p_list_utility = []
p_list_synchgenerator = []
p_list_pv = []
p_list_wind = []
p_list_load = []
p_list_line = []
p_list_cable = []
p_list_directconnection = []
p_list_transformer = []
p_list_bus = []
p_list_wiredata = []
p_list_linecode = []


class Power(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in):
        self.object_ID_number = object_ID_number_in
        self.object_name = object_name_in
        self.operational_status = operational_status_in

    @abc.abstractmethod
    def inc_object_ID_number_iter(cls):
        '''Method that should do something.'''


class PowerArc(Power):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 from_bus_object_ID_in, from_bus_component_ID_in,
                 to_bus_object_ID_in, to_bus_component_ID_in):
        self.current_1_magnitude = np.float32(0.0)
        self.current_1_angle = np.float32(0.0)
        self.real_power_entering = np.float32(0.0)
        self.real_power_leaving = np.float32(0.0)
        self.reactive_power_entering = np.float32(0.0)
        self.reactive_power_leaving = np.float32(0.0)
        self.from_bus_object_ID = from_bus_object_ID_in
        self.from_bus_component_ID = from_bus_component_ID_in
        self.to_bus_object_ID = to_bus_object_ID_in
        self.to_bus_component_ID = to_bus_component_ID_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in)

    @abc.abstractmethod
    def inc_component_count(self):
        '''Method that should do something.'''

    @abc.abstractmethod
    def dec_component_count(self):
        '''Method that should do something.'''


class PowerNode(Power):
    __metaclass__ = abc.ABCMeta
    swing_component_ID_number = np.int32(0)
    swing_object_ID_number = np.int32(0)

    @abc.abstractmethod
    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 latitude_in, longitude_in):
        self.LL_voltage = np.float32(0.0)
        self.voltage_1_magnitude = np.float32(0.0)
        self.voltage_1_angle = np.float32(0.0)
        self.voltage_1_pu = np.float32(0.0)
        self.latitude = latitude_in
        self.longitude = longitude_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in)

    @abc.abstractmethod
    def inc_component_count(self):
        '''Method that should do something.'''

    @abc.abstractmethod
    def dec_component_count(self):
        '''Method that should do something.'''


class LineCode(Power):
    COMPONENT_ID_NUMBER = LINECODE_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 continuous_ampacity_in, emergency_ampacity_in, r_1_in, x_1_in,
                 r_0_in, x_0_in):
        self.continuous_ampacity = continuous_ampacity_in
        self.emergency_ampacity = emergency_ampacity_in
        self.r_1 = r_1_in
        self.x_1 = x_1_in
        self.r_0 = r_0_in
        self.x_0 = x_0_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in)

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # INCOMPLETE
    def updateAttributes(self, number_of_cables_in, continuous_ampacity_in,
                         emergency_ampacity_in, r_1_in, x_1_in,
                         r_0_in, x_0_in):
        self.continuous_ampacity = continuous_ampacity_in * number_of_cables_in
        self.emergency_ampacity = emergency_ampacity_in * number_of_cables_in
        self.r_1 = r_1_in / number_of_cables_in
        self.x_1 = x_1_in / number_of_cables_in
        self.r_0 = r_0_in / number_of_cables_in
        self.x_0 = x_0_in / number_of_cables_in

    def printobject(self):
        print('continuous_ampacity', self.continuous_ampacity)
        print('emergency_ampacity', self.emergency_ampacity)
        print('r_1', self.r_1)
        print('x_1', self.x_1)
        print('r_0', self.r_0)
        print('x_0', self.x_0)

    @staticmethod
    def helpclass():
        print('\nLineCode Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'continuous_ampacity'})
        print({'float32': 'emergency_ampacity'})
        print({'float32': 'r_1'})
        print({'float32': 'x_1'})
        print({'float32': 'r_0'})
        print({'float32': 'x_0'})
        print('')


class WireData(Power):
    COMPONENT_ID_NUMBER = WIREDATA_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 phase_resistance_50_C_in, phase_GMR_in,
                 phase_continuous_ampacity_in, phase_emergency_ampacity_in,
                 phase_diameter_in, neutral_resistance_50_C_in=None,
                 neutral_GMR_in=None, neutral_continuous_ampacity_in=None,
                 neutral_emergency_ampacity_in=None, neutral_diameter_in=None):
        self.phase_resistance_50_C = phase_resistance_50_C_in
        self.phase_GMR = phase_GMR_in
        self.phase_continuous_ampacity = phase_continuous_ampacity_in
        self.phase_emergency_ampacity = phase_emergency_ampacity_in
        self.phase_diameter = phase_diameter_in
        self.neutral_resistance_50_C = neutral_resistance_50_C_in
        self.neutral_GMR = neutral_GMR_in
        self.neutral_continuous_ampacity = neutral_continuous_ampacity_in
        self.neutral_emergency_ampacity = neutral_emergency_ampacity_in
        self.neutral_diameter = neutral_diameter_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in)

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # INCOMPLETE
    def updateAttributes(self, phase_resistance_50_C_in, phase_GMR_in,
                         phase_continuous_ampacity_in,
                         phase_emergency_ampacity_in,
                         phase_diameter_in, neutral_resistance_50_C_in=None,
                         neutral_GMR_in=None,
                         neutral_continuous_ampacity_in=None,
                         neutral_emergency_ampacity_in=None,
                         neutral_diameter_in=None):
        self.phase_resistance_50_C = phase_resistance_50_C_in
        self.phase_GMR = phase_GMR_in
        self.phase_continuous_ampacity = phase_continuous_ampacity_in
        self.phase_emergency_ampacity = phase_emergency_ampacity_in
        self.phase_diameter = phase_diameter_in
        self.neutral_resistance_50_C = neutral_resistance_50_C_in
        self.neutral_GMR = neutral_GMR_in
        self.neutral_continuous_ampacity = neutral_continuous_ampacity_in
        self.neutral_emergency_ampacity = neutral_emergency_ampacity_in
        self.neutral_diameter = neutral_diameter_in

    def printobject3(self):
        print('phase_resistance_50_C', self.phase_resistance_50_C)
        print('phase_GMR', self.phase_GMR)
        print('phase_continuous_ampacity', self.phase_continuous_ampacity)
        print('phase_emergency_ampacity', self.phase_emergency_ampacity)
        print('phase_diameter', self.phase_diameter)

    def printobject4(self):
        print('neutral_resistance_50_C', self.neutral_resistance_50_C)
        print('neutral_GMR', self.neutral_GMR)
        print('neutral_continuous_ampacity', self.neutral_continuous_ampacity)
        print('neutral_emergency_ampacity', self.neutral_emergency_ampacity)
        print('neutral_diameter', self.neutral_diameter)

    @staticmethod
    def helpclass():
        print('\nWireData Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'phase_resistance_50_C'})
        print({'float32': 'phase_GMR'})
        print({'float32': 'phase_continuous_ampacity'})
        print({'float32': 'phase_emergency_ampacity'})
        print({'float32': 'phase_diameter'})
        print('')
        print({'float32': 'neutral_resistance_50_C'})
        print({'float32': 'neutral_GMR'})
        print({'float32': 'neutral_continuous_ampacity'})
        print({'float32': 'neutral_emergency_ampacity'})
        print({'float32': 'neutral_diameter'})
        print('')


class Cable(PowerArc):
    COMPONENT_ID_NUMBER = CABLE_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 from_bus_object_ID_in, from_bus_component_ID_in,
                 to_bus_object_ID_in, to_bus_component_ID_in,
                 linecode_object_ID_in, voltage_rating_in, length_in,
                 number_of_cables_in):
        self.linecode_object_ID = linecode_object_ID_in
        self.voltage_rating = voltage_rating_in
        self.length = length_in
        self.number_of_cables = number_of_cables_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         from_bus_object_ID_in, from_bus_component_ID_in,
                         to_bus_object_ID_in, to_bus_component_ID_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global branch_count
        branch_count += 1

    # globalmethod
    def dec_component_count(self):
        global branch_count
        branch_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('from_bus_object_ID', self.from_bus_object_ID)
        print('from_bus_component_ID', self.from_bus_component_ID)
        print('to_bus_object_ID', self.to_bus_object_ID)
        print('to_bus_component_ID', self.to_bus_component_ID)
        print('linecode_object_ID', self.linecode_object_ID)
        print('voltage_rating', self.voltage_rating)
        print('length', self.length)
        print('number_of_cables', self.number_of_cables)
        p_list_linecode[self.linecode_object_ID - 1].printobject()
        print('')

    @staticmethod
    def helpclass():
        print('\nCable Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'int32': 'from_bus_object_ID'})
        print({'int32': 'from_bus_component_ID'})
        print({'int32': 'to_bus_object_ID'})
        print({'int32': 'to_bus_component_ID'})
        print({'int32': 'linecode_object_ID'})
        print({'float32': 'voltage_rating'})
        print({'float32': 'length'})
        print({'int32': 'number_of_cables'})
        print('')


class DirectConnection(PowerArc):
    COMPONENT_ID_NUMBER = DIRECTCONNECTION_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 from_bus_object_ID_in, from_bus_component_ID_in,
                 to_bus_object_ID_in, to_bus_component_ID_in):
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         from_bus_object_ID_in, from_bus_component_ID_in,
                         to_bus_object_ID_in, to_bus_component_ID_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global branch_count
        branch_count += 1

    # globalmethod
    def dec_component_count(self):
        global branch_count
        branch_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('from_bus_object_ID', self.from_bus_object_ID)
        print('from_bus_component_ID', self.from_bus_component_ID)
        print('to_bus_object_ID', self.to_bus_object_ID)
        print('to_bus_component_ID', self.to_bus_component_ID)
        print('')

    @staticmethod
    def helpclass():
        print('\nDirectConnection Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'int32': 'from_bus_object_ID'})
        print({'int32': 'from_bus_component_ID'})
        print({'int32': 'to_bus_object_ID'})
        print({'int32': 'to_bus_component_ID'})
        print('')


class OverheadLine(PowerArc):
    COMPONENT_ID_NUMBER = OVERHEADLINE_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 from_bus_object_ID_in, from_bus_component_ID_in,
                 to_bus_object_ID_in, to_bus_component_ID_in,
                 wiredata_object_ID_in, number_of_conductors_in,
                 x_1_coordinate_in,
                 x_2_coordinate_in, x_3_coordinate_in, h_1_coordinate_in,
                 h_2_coordinate_in,
                 h_3_coordinate_in, length_in, soil_resistivity_in,
                 kron_reduction_in,
                 x_4_coordinate_in=None, h_4_coordinate_in=None):
        self.wiredata_object_ID = wiredata_object_ID_in
        self.number_of_conductors = number_of_conductors_in
        self.x_1_coordinate = x_1_coordinate_in
        self.x_2_coordinate = x_2_coordinate_in
        self.x_3_coordinate = x_3_coordinate_in
        self.h_1_coordinate = h_1_coordinate_in
        self.h_2_coordinate = h_2_coordinate_in
        self.h_3_coordinate = h_3_coordinate_in
        self.length = length_in
        self.soil_resistivity = soil_resistivity_in
        self.x_4_coordinate = x_4_coordinate_in
        self.h_4_coordinate = h_4_coordinate_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         from_bus_object_ID_in, from_bus_component_ID_in,
                         to_bus_object_ID_in, to_bus_component_ID_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global branch_count
        branch_count += 1

    # globalmethod
    def dec_component_count(self):
        global branch_count
        branch_count -= 1

    def printobject(self):
        if self.number_of_conductors == 3:
            print('object_ID_number', self.object_ID_number)
            print('object_name', self.object_name)
            print('operational_status', self.operational_status)
            print('from_bus_object_ID', self.from_bus_object_ID)
            print('from_bus_component_ID', self.from_bus_component_ID)
            print('to_bus_object_ID', self.to_bus_object_ID)
            print('to_bus_component_ID', self.to_bus_component_ID)
            print('wiredata_object_ID', self.wiredata_object_ID)
            print('number_of_conductors', self.number_of_conductors)
            p_list_wiredata[self.wiredata_object_ID - 1].printobject3()
            print('x_1_coordinate', self.x_1_coordinate)
            print('x_2_coordinate', self.x_2_coordinate)
            print('x_3_coordinate', self.x_3_coordinate)
            print('h_1_coordinate', self.h_1_coordinate)
            print('h_2_coordinate', self.h_2_coordinate)
            print('h_3_coordinate', self.h_3_coordinate)
            print('length', self.length)
            print('soil_resistivity', self.soil_resistivity)
            print('kron_reduction', self.kron_reduction)
            print('')
        else:
            print('object_ID_number', self.object_ID_number)
            print('object_name', self.object_name)
            print('operational_status', self.operational_status)
            print('from_bus_object_ID', self.from_bus_object_ID)
            print('from_bus_component_ID', self.from_bus_component_ID)
            print('to_bus_object_ID', self.to_bus_object_ID)
            print('to_bus_component_ID', self.to_bus_component_ID)
            print('wiredata_object_ID', self.wiredata_object_ID)
            print('number_of_conductors', self.number_of_conductors)
            p_list_wiredata[self.wiredata_object_ID - 1].printobject3()
            print('x_1_coordinate', self.x_1_coordinate)
            print('x_2_coordinate', self.x_2_coordinate)
            print('x_3_coordinate', self.x_3_coordinate)
            print('h_1_coordinate', self.h_1_coordinate)
            print('h_2_coordinate', self.h_2_coordinate)
            print('h_3_coordinate', self.h_3_coordinate)
            print('length', self.length)
            print('soil_resistivity', self.soil_resistivity)
            print('kron_reduction', self.kron_reduction)
            p_list_wiredata[self.wiredata_object_ID - 1].printobject4()
            print('x_4_coordinate', self.x_4_coordinate)
            print('h_4_coordinate', self.h_4_coordinate)
            print('')

    @staticmethod
    def helpclass():
        print('\nOverheadLine Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'int32': 'from_bus_object_ID'})
        print({'int32': 'from_bus_component_ID'})
        print({'int32': 'to_bus_object_ID'})
        print({'int32': 'to_bus_component_ID'})
        print({'int32': 'wiredata_object_ID'})
        print({'int32': 'number_of_conductors'})
        print({'float32': 'x_1_coordinate'})
        print({'float32': 'x_2_coordinate'})
        print({'float32': 'x_3_coordinate'})
        print({'float32': 'h_1_coordinate'})
        print({'float32': 'h_2_coordinate'})
        print({'float32': 'h_3_coordinate'})
        print({'float32': 'length'})
        print({'float32': 'soil_resistivity'})
        print({'bool_': 'kron_reduction'})
        print('')
        print({'float32': 'x_4_coordinate'})
        print({'float32': 'h_4_coordinate'})
        print('')


class TwoWindingTransformer(PowerArc):
    COMPONENT_ID_NUMBER = TWOWINDINGTRANSFORMER_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 from_bus_object_ID_in, from_bus_component_ID_in,
                 to_bus_object_ID_in, to_bus_component_ID_in,
                 from_bus_voltage_rating_in, to_bus_voltage_rating_in,
                 from_bus_wiring_in, to_bus_wiring_in,
                 power_rating_in, x_percent_in, r_percent_in, tap_percent_in,
                 number_of_taps_in, tap_side_in, min_tap_in, max_tap_in):
        self.from_bus_voltage_rating = from_bus_voltage_rating_in
        self.to_bus_voltage_rating = to_bus_voltage_rating_in
        self.from_bus_wiring = from_bus_wiring_in
        self.to_bus_wiring = to_bus_wiring_in
        self.power_rating = power_rating_in
        self.x_percent = x_percent_in
        self.r_percent = r_percent_in
        self.tap_percent = tap_percent_in
        self.number_of_taps = number_of_taps_in
        self.tap_side = tap_side_in
        self.min_tap = min_tap_in
        self.max_tap = max_tap_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         from_bus_object_ID_in, from_bus_component_ID_in,
                         to_bus_object_ID_in, to_bus_component_ID_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global transformer_count
        transformer_count += 1

    # globalmethod
    def dec_component_count(self):
        global transformer_count
        transformer_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('from_bus_object_ID', self.from_bus_object_ID)
        print('from_bus_component_ID', self.from_bus_component_ID)
        print('to_bus_object_ID', self.to_bus_object_ID)
        print('to_bus_component_ID', self.to_bus_component_ID)
        print('from_bus_voltage_rating', self.from_bus_voltage_rating)
        print('to_bus_voltage_rating', self.to_bus_voltage_rating)
        print('from_bus_wiring', self.from_bus_wiring)
        print('to_bus_wiring', self.to_bus_wiring)
        print('power_rating', self.power_rating)
        print('x_percent', self.x_percent)
        print('r_percent', self.r_percent)
        print('tap_percent', self.tap_percent)
        print('number_of_taps', self.number_of_taps)
        print('tap_side', self.tap_side)
        print('min_tap', self.min_tap)
        print('max_tap', self.max_tap)
        print('')

    @staticmethod
    def helpclass():
        print('\nTwoWindingTransformer Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'int32': 'from_bus_object_ID'})
        print({'int32': 'from_bus_component_ID'})
        print({'int32': 'to_bus_object_ID'})
        print({'int32': 'to_bus_component_ID'})
        print({'float32': 'from_bus_voltage_rating'})
        print({'float32': 'to_bus_voltage_rating'})
        print({'int32': 'from_bus_wiring'})
        print({'int32': 'to_bus_wiring'})
        print({'float32': 'power_rating'})
        print({'float32': 'x_percent'})
        print({'float32': 'r_percent'})
        print({'float32': 'tap_percent'})
        print({'int32': 'number_of_taps'})
        print({'bool_': 'tap_side'})
        print({'float32': 'min_tap'})
        print({'float32': 'max_tap'})
        print('')


class Bus(PowerNode):
    COMPONENT_ID_NUMBER = OVERHEADLINE_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 latitude_in, longitude_in,
                 nominal_LL_voltage_in):
        self.nominal_LL_voltage = nominal_LL_voltage_in
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         latitude_in, longitude_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global bus_count
        bus_count += 1

    # globalmethod
    def dec_component_count(self):
        global bus_count
        bus_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('latitude', self.latitude)
        print('longitude', self.longitude)
        print('nominal_LL_voltage', self.nominal_LL_voltage)
        print('')

    @staticmethod
    def helpclass():
        print('\nBus Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'latitude'})
        print({'float32': 'longitude'})
        print({'float32': 'nominal_LL_voltage'})
        print('')


class Load(PowerNode):
    COMPONENT_ID_NUMBER = LOAD_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 latitude_in, longitude_in,
                 nominal_LL_voltage_in, power_rating_in, pf_percent_in,
                 pf_type_in,
                 min_pu_voltage_in, wiring_in, load_model_in):
        self.power_rating = power_rating_in
        self.pf_percent = pf_percent_in
        self.pf_type = pf_type_in
        self.min_pu_voltage = min_pu_voltage_in
        self.wiring = wiring_in
        self.load_model = load_model_in
        self.nominal_LL_voltage = nominal_LL_voltage_in
        self.current_rating = np.float32(0.0)
        self.current_1_magnitude = np.float32(0.0)
        self.current_1_angle = np.float32(0.0)
        self.real_power = np.float32(0.0)
        self.reactive_power = np.float32(0.0)
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         latitude_in, longitude_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global load_count
        load_count += 1

    # globalmethod
    def dec_component_count(self):
        global load_count
        load_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('latitude', self.latitude)
        print('longitude', self.longitude)
        print('nominal_LL_voltage', self.nominal_LL_voltage)
        print('power_rating', self.power_rating)
        print('pf_percent', self.pf_percent)
        print('pf_type', self.pf_type)
        print('min_pu_voltage', self.min_pu_voltage)
        print('wiring', self.wiring)
        print('load_model', self.load_model)
        print('')

    @staticmethod
    def helpclass():
        print('\nLoad Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'latitude'})
        print({'float32': 'longitude'})
        print({'float32': 'nominal_LL_voltage'})
        print({'float32': 'power_rating'})
        print({'float32': 'pf_percent'})
        print({'int32': 'pf_type'})
        print({'float32': 'min_pu_voltage'})
        print({'int32': 'wiring'})
        print({'int32': 'load_model'})
        print('')


class SynchGenerator(PowerNode):
    COMPONENT_ID_NUMBER = SYNCHGENERATOR_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 latitude_in, longitude_in,
                 nominal_LL_voltage_in, stiffness_in, power_rating_in,
                 RPM_rating_in,
                 number_of_poles_in, pf_percent_in, wiring_in):
        self.stiffness = stiffness_in
        self.power_rating = power_rating_in
        self.nominal_LL_voltage = nominal_LL_voltage_in
        self.RPM_rating = RPM_rating_in
        self.number_of_poles = number_of_poles_in
        self.pf_percent = pf_percent_in
        self.wiring = wiring_in
        self.current_1_magnitude = np.float32(0.0)
        self.current_1_angle = np.float32(0.0)
        self.real_power = np.float32(0.0)
        self.reactive_power = np.float32(0.0)
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         latitude_in, longitude_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global generator_count
        generator_count += 1

    # globalmethod
    def dec_component_count(self):
        global generator_count
        generator_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('latitude', self.latitude)
        print('longitude', self.longitude)
        print('nominal_LL_voltage', self.nominal_LL_voltage)
        print('stiffness', self.stiffness)
        print('power_rating', self.power_rating)
        print('RPM_rating', self.RPM_rating)
        print('number_of_poles', self.number_of_poles)
        print('pf_percent', self.pf_percent)
        print('wiring', self.wiring)
        print()

    @staticmethod
    def helpclass():
        print('\nSynchGenerator Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'latitude'})
        print({'float32': 'longitude'})
        print({'float32': 'nominal_LL_voltage'})
        print({'bool_': 'stiffness'})
        print({'float32': 'power_rating'})
        print({'int32': 'RPM_rating'})
        print({'int32': 'number_of_poles'})
        print({'float32': 'pf_percent'})
        print({'int32': 'wiring'})
        print('')


class Utility(PowerNode):
    COMPONENT_ID_NUMBER = UTILITY_ID
    object_ID_number_iter = np.int32(1)

    def __init__(self, object_ID_number_in, object_name_in,
                 operational_status_in,
                 latitude_in, longitude_in,
                 nominal_LL_voltage_in, base_power_in, voltage_angle_in,
                 short_circuit_3_phase_in,
                 short_circuit_SLG_in, stiffness_in, r_1_in, r_0_in,
                 x_1_in, x_0_in):
        self.nominal_LL_voltage = nominal_LL_voltage_in
        self.base_power = base_power_in
        self.voltage_angle = voltage_angle_in
        self.short_circuit_3_phase = short_circuit_3_phase_in
        self.short_circuit_SLG = short_circuit_SLG_in
        self.stiffness = stiffness_in
        self.r_1 = r_1_in
        self.r_0 = r_0_in
        self.x_1 = x_1_in
        self.x_0 = x_0_in
        self.current_1_magnitude = np.float32(0.0)
        self.current_1_angle = np.float32(0.0)
        super().__init__(object_ID_number_in, object_name_in,
                         operational_status_in,
                         latitude_in, longitude_in)
        self.inc_component_count()

    def __del__(self):
        self.dec_component_count()

    @classmethod
    def inc_object_ID_number_iter(cls):
        cls.object_ID_number_iter += 1

    # globalmethod
    def inc_component_count(self):
        global utility_count
        utility_count += 1

    # globalmethod
    def dec_component_count(self):
        global utility_count
        utility_count -= 1

    def printobject(self):
        print('object_ID_number', self.object_ID_number)
        print('object_name', self.object_name)
        print('operational_status', self.operational_status)
        print('latitude', self.latitude)
        print('longitude', self.longitude)
        print('nominal_LL_voltage', self.nominal_LL_voltage)
        print('base_power', self.base_power)
        print('voltage_angle', self.voltage_angle)
        print('short_circuit_3_phase', self.short_circuit_3_phase)
        print('short_circuit_SLG', self.short_circuit_SLG)
        print('stiffness', self.stifness)
        print('r_1', self.r_1)
        print('r_0', self.r_0)
        print('x_1', self.x_1)
        print('x_0', self.x_0)
        print('')

    @staticmethod
    def helpclass():
        print('\nUtility Class')
        print('-----------------------------')
        print({'DATA TYPE': 'VARIABLE NAME'})
        print('-----------------------------')
        print({'int32': 'object_ID_number'})
        print({'string': 'object_name'})
        print({'bool_': 'operational_status'})
        print({'float32': 'latitude'})
        print({'float32': 'longitude'})
        print({'float32': 'nominal_LL_voltage'})
        print({'float32': 'base_power'})
        print({'float32': 'voltage_angle'})
        print({'float32': 'short_circuit_3_phase'})
        print({'float32': 'short_circuit_SLG'})
        print({'bool_': 'stiffness'})
        print({'float32': 'r_1'})
        print({'float32': 'r_0'})
        print({'float32': 'x_1'})
        print({'float32': 'x_0'})
        print('')



        ##### OLD STUFF #####

        # class Cable(PowerArc):
        # 	COMPONENT_ID_NUMBER = CABLE_ID
        # 	object_ID_number_iter = np.int32(1)

        # 	def __init__(self, object_name_in, operational_status_in, object_ID_number_in,
        # 		linecode_object_ID_in, voltage_rating_in, length_in, number_of_cables_in,
        # 		continuous_ampacity_in, emergency_ampacity_in, r_1_in, x_1_in,
        # 		r_0_in, x_0_in,
        # 		**kwargs):
        # 		self.linecode_object_ID = linecode_object_ID_in
        # 		self.voltage_rating = voltage_rating_in
        # 		self.length = length_in
        # 		self.number_of_cables = number_of_cables_in
        # 		continuous_ampacity_in = continuous_ampacity_in * number_of_cables_in
        # 		emergency_ampacity_in = emergency_ampacity_in * number_of_cables_in
        # 		r_1_in = r_1_in / number_of_cables_in
        # 		x_1_in = x_1_in / number_of_cables_in
        # 		r_0_in = r_0_in / number_of_cables_in
        # 		x_0_in = x_0_in / number_of_cables_in

        # 		if not self.lineCodeExists():
        # 			linecodekwargs = {'operational_status_in': np.bool_(True)}
        # 			templinecode = LineCode(number_of_cables_in, continuous_ampacity_in, emergency_ampacity_in, r_1_in, x_1_in, r_0_in,
        # 				x_0_in, **linecodekwargs)
        # 			p_list_linecode.append(templinecode)
        # 			templinecode = None
        # 			linecodekwargs = None
        # 			self.linecode_object_ID = len(p_list_linecode)

        # 		p_list_linecode[self.linecode_object_ID - 1].updateAttributes(number_of_cables_in, continuous_ampacity_in, emergency_ampacity_in, r_1_in, x_1_in,
        # 			r_0_in, x_0_in)
        # 		kwargs['object_ID_number_in'] = Cable.object_ID_number_iter
        # 		kwargs['object_name_in'] = str(number_of_cables_in)+'cable_'+str(Cable.object_ID_number_iter)
        # 		super().__init__(**kwargs)
        # 		self.inc_object_ID_number_iter()
        # 		self.inc_component_count()

        # 	def lineCodeExists(self):
        # 		try:
        # 			return p_list_linecode[self.linecode_object_ID - 1]
        # 		except:
        # 			return False

        # class OverheadLine(PowerArc):
        # 	COMPONENT_ID_NUMBER = OVERHEADLINE_ID
        # 	object_ID_number_iter = np.int32(1)

        # 	def __init__(self, wiredata_object_ID_in, number_of_conductors_in, phase_resistance_50_C_in, phase_GMR_in,
        # 		phase_continuous_ampacity_in, phase_emergency_ampacity_in, phase_diameter_in, x_1_coordinate_in,
        # 		x_2_coordinate_in, x_3_coordinate_in, h_1_coordinate_in, h_2_coordinate_in,
        # 		h_3_coordinate_in, length_in, soil_resistivity_in, neutral_resistance_50_C_in=None,
        # 		neutral_GMR_in=None, neutral_continuous_ampacity_in=None, neutral_emergency_ampacity_in=None,
        # 		neutral_diameter_in=None, x_4_coordinate_in=None, h_4_coordinate_in=None,
        # 		**kwargs):
        # 		self.wiredata_object_ID = wiredata_object_ID_in
        # 		self.number_of_conductors = number_of_conductors_in
        # 		self.x_1_coordinate = x_1_coordinate_in
        # 		self.x_2_coordinate = x_2_coordinate_in
        # 		self.x_3_coordinate = x_3_coordinate_in
        # 		self.h_1_coordinate = h_1_coordinate_in
        # 		self.h_2_coordinate = h_2_coordinate_in
        # 		self.h_3_coordinate = h_3_coordinate_in
        # 		self.length = length_in
        # 		self.soil_resistivity = soil_resistivity_in
        # 		self.x_4_coordinate = x_4_coordinate_in
        # 		self.h_4_coordinate = h_4_coordinate_in
        # 		self.nominal_LL_voltage = np.float32(0.0)

        # 		if not self.wireDataExists():
        # 			wiredatakwargs = {'operational_status_in': np.bool_(True)}
        # 			tempwiredata = WireData(phase_resistance_50_C_in, phase_GMR_in, phase_continuous_ampacity_in, phase_emergency_ampacity_in,
        # 				phase_diameter_in, neutral_resistance_50_C_in, neutral_GMR_in, neutral_continuous_ampacity_in, neutral_emergency_ampacity_in, neutral_diameter_in,
        # 				**wiredatakwargs)
        # 			p_list_wiredata.append(tempwiredata)
        # 			tempwiredata = None
        # 			wiredatakwargs = None
        # 			self.wiredata_object_ID = len(p_list_wiredata)

        # 		p_list_wiredata[self.wiredata_object_ID - 1].updateAttributes(phase_resistance_50_C_in, phase_GMR_in, phase_continuous_ampacity_in, phase_emergency_ampacity_in,
        # 			phase_diameter_in, neutral_resistance_50_C_in, neutral_GMR_in, neutral_continuous_ampacity_in, neutral_emergency_ampacity_in, neutral_diameter_in)
        # 		kwargs['object_ID_number_in'] = OverheadLine.object_ID_number_iter
        # 		kwargs['object_name_in'] = 'overhead_line_'+str(OverheadLine.object_ID_number_iter)
        # 		super().__init__(**kwargs)
        # 		self.inc_object_ID_number_iter()
        # 		self.inc_component_count()

        # def wireDataExists(self):
        # 	try:
        # 		return p_list_wiredata[self.wiredata_object_ID - 1]
        # 	except:
        # 		return False

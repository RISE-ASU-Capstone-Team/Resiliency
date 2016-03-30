class Simulation:
    POWER = 0
    WATER = 1
    ROAD = 2


class Power:
    LOAD = 0
    SYNCHRONOUS_GENERATOR = 1
    BUS = 2
    UTILITY = 3

    TWO_WINDING_TRANSFORMER = 0
    DIRECT_CONNECTION = 1
    CABLE = 2
    OVERHEAD_LINE = 3

    PHASE = 0
    NEUTRAL = 1


class Load:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    IS_BUS = 3
    VOLTAGE_1_MAGNITUDE = 4
    VOLTAGE_1_ANGLE = 5
    VOLTAGE_1_PU = 6
    TYPE = 7
    LATITUDE = 8
    LONGITUDE = 9
    LL_VOLTAGE = 11
    NOMINAL_VOLTAGE = 12
    POWER_RATING = 14
    POWER_FACTOR_PERCENT = 15
    POWER_FACTOR_TYPE = 16
    MIN_PU_VOLTAGE = 17
    WIRING = 18
    LOAD_MODEL = 19
    CURRENT_RATING = 20
    CURRENT_1_MAGNITUDE = 21
    CURRENT_1_ANGLE = 22
    REAL_POWER = 23
    REACTIVE_POWER = 24


class SynchronousGenerator:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    IS_BUS = 3
    VOLTAGE_1_MAGNITUDE = 4
    VOLTAGE_1_ANGLE = 5
    VOLTAGE_1_PU = 6
    TYPE = 7
    LATITUDE = 8
    LONGITUDE = 9
    LL_VOLTAGE = 11
    NOMINAL_VOLTAGE = 12
    STIFFNESS = 14
    POWER_RATING = 15
    RPM_RATING = 16
    NUMBER_OF_POLES = 17
    POWER_FACTOR_PERCENT = 18
    WIRING = 19
    CURRENT_1_MAGNITUDE = 20
    CURRENT_1_ANGLE = 21
    REAL_POWER = 22
    REACTIVE_POWER = 23


class Bus:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    IS_BUS = 3
    VOLTAGE_1_MAGNITUDE = 4
    VOLTAGE_1_ANGLE = 5
    VOLTAGE_1_PU = 6
    TYPE = 7
    LATITUDE = 8
    LONGITUDE = 9
    LL_VOLTAGE = 11
    NOMINAL_VOLTAGE = 12


class Utility:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    IS_BUS = 3
    VOLTAGE_1_MAGNITUDE = 4
    VOLTAGE_1_ANGLE = 5
    VOLTAGE_1_PU = 6
    TYPE = 7
    LATITUDE = 8
    LONGITUDE = 9
    BASE_POWER = 14
    LL_VOLTAGE = 11
    NOMINAL_VOLTAGE = 12
    VOLTAGE_ANGLE = 15
    SHORT_CIRCUIT_3_PHASE = 16
    SHORT_CIRCUIT_SLG = 17
    STIFFNESS = 18
    R_1 = 19
    X_1 = 20
    R_0 = 21
    X_0 = 22
    CURRENT_1_MAGNITUDE = 23
    CURRENT_1_ANGLE = 24


class TwoWindingTransformer:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    CURRENT_1_MAGNITUDE = 3
    CURRENT_1_ANGLE = 4
    REAL_POWER_ENTERING = 5
    REACTIVE_POWER_ENTERING = 6
    REAL_POWER_LEAVING = 7
    REACTIVE_POWER_LEAVING = 8
    TYPE = 9
    FROM_BUS = 10
    TO_BUS = 11
    FROM_BUS_VOLTAGE_RATING = 14
    TO_BUS_VOLTAGE_RATING = 15
    FROM_BUS_WIRING = 16
    TO_BUS_WIRING = 17
    POWER_RATING = 18
    X_PERCENT = 19
    R_PERCENT = 20
    TAP_PERCENT = 21
    TAP_SIDE = 22
    MIN_TAP = 23
    MAX_TAP = 24


class DirectConnection:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    CURRENT_1_MAGNITUDE = 3
    CURRENT_1_ANGLE = 4
    REAL_POWER_ENTERING = 5
    REACTIVE_POWER_ENTERING = 6
    REAL_POWER_LEAVING = 7
    REACTIVE_POWER_LEAVING = 8
    TYPE = 9
    FROM_BUS = 10
    TO_BUS = 11
    FROM_BUS_VOLTAGE_RATING = 14
    TO_BUS_VOLTAGE_RATING = 15


class Cable:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    CURRENT_1_MAGNITUDE = 3
    CURRENT_1_ANGLE = 4
    REAL_POWER_ENTERING = 5
    REACTIVE_POWER_ENTERING = 6
    REAL_POWER_LEAVING = 7
    REACTIVE_POWER_LEAVING = 8
    TYPE = 9
    FROM_BUS = 10
    TO_BUS = 11
    LINECODE_OBJECT_ID = 14
    VOLTAGE_RATING = 15
    LENGTH = 16
    NUMBER_OF_CABLES = 17


class OverheadLine:
    ID = 0
    NAME = 1
    OPERATIONAL_STATUS = 2
    CURRENT_1_MAGNITUDE = 3
    CURRENT_1_ANGLE = 4
    REAL_POWER_ENTERING = 5
    REACTIVE_POWER_ENTERING = 6
    REAL_POWER_LEAVING = 7
    REACTIVE_POWER_LEAVING = 8
    TYPE = 9
    FROM_BUS = 10
    TO_BUS = 11
    WIREDATA_OBJECT_ID = 14
    NUMBER_OF_CONDUCTORS = 15
    LENGTH = 16
    SOIL_RESISTIVITY = 17
    X_1 = 18
    X_2 = 19
    X_3 = 20
    Y_1 = 21
    Y_2 = 22
    Y_3 = 23
    H_1 = 24
    H_2 = 25
    H_3 = 26
    X_4 = 27
    Y_4 = 28
    H_4 = 29
    NOMINAL_LL_VOLTAGE = 30


class WireData:
    ID = 0
    NAME = 1
    RESISTANCE_50_C = 2
    CONTINUOUS_AMPACITY = 3
    EMERGENCY_AMPACITY = 4
    DIAMETER = 5
    GMR = 6
    TYPE = 7
    WIRE_TYPE = 8


class LineCode:
    ID = 0
    NAME = 1
    R_1 = 2
    X_1 = 3
    R_0 = 4
    X_0 = 5
    CONTINUOUS_AMPACITY = 6
    EMERGENCY_AMPACITY = 7


class WireType:
    PHASE = 0
    NEUTRAL = 1


class OpenDSS:
    ELEMENT = 'Element'
    VSOURCE = 'Vsource'
    SOURCE = 'SOURCE'
    LINE = 'Line'
    TRANSFORMER = 'Transformer'
    GENERATOR = 'Generator'
    LOAD = 'load'

    CURRENT_1_MAGNITUDE = 1
    CURRENT_1_ANGLE = 2


class Tables:
    NODE = 'client_node'
    CONNECTION = 'client_connection'
    BUS = 'client_bus'
    CABLE = 'client_cable'
    DB_CHANGE = 'client_dbchanges'
    DIRECT = 'client_directconnection'
    LINE_CODE = 'client_linecode'
    LOAD = 'client_load'
    OVERHEAD = 'client_overheadline'
    POWER = 'client_power'
    SYNC_GEN = 'client_syncgenerator'
    TRANSFORMER = 'client_twowindingtransformer'
    UTILITY = 'client_utility'
    WIRE_DATA = 'client_wiredata'


def comp_type_eval(comp_type):
        if comp_type == Power.LOAD:
            return Tables.LOAD
        elif comp_type == Power.BUS:
            return Tables.BUS
        elif comp_type == Power.CABLE:
            return Tables.CABLE
        elif comp_type == Power.DIRECT_CONNECTION:
            return Tables.DIRECT
        elif comp_type == Power.OVERHEAD_LINE:
            return Tables.OVERHEAD
        elif comp_type == Power.SYNCHRONOUS_GENERATOR:
            return Tables.SYNC_GEN
        elif comp_type == Power.TWO_WINDING_TRANSFORMER:
            return Tables.TRANSFORMER
        elif comp_type == Power.UTILITY:
            return Tables.UTILITY

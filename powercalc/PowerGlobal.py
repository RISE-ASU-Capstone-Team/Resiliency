import numpy as np


# PowerAccessories
WIREDATA_ID = np.int32(1000)
LINECODE_ID = np.int32(1001)

# PowerArcs
CABLE_ID = np.int32(1100)
DIRECTCONNECTION_ID = np.int32(1101)
OVERHEADLINE_ID = np.int32(1102)
TWOWINDINGTRANSFORMER_ID = np.int32(1103)

# PowerNodes
BUS_ID = np.int32(1200)
LOAD_ID = np.int32(1201)
SYNCHGENERATOR_ID = np.int32(1202)
UTILITY_ID = np.int32(1203)

# DefaultsForRISE
DEFAULTPU = np.float32(1.0)
DEFAULTPHASES = np.int32(3)
DEFAULTWINDINGS = np.int32(2)


# This stuff will change due to the user
# C or F
temperature_units = 'C'
celsius_ambient_temp = np.float32(0)
fahrenheit_ambient_temp = np.float32(0)
# V or kV
voltage_units = 'V'
# A or kA
current_units = 'A'
# kVar or MVar
power_units = 'kVa'
# 50 or 60
base_frequency = np.int32(60)
# twt transformers
transformer_count = np.int32(0)
# cables, direct connections, and overhead lines
branch_count = np.int32(0)
# busbars
bus_count = np.int32(0)
# loads
load_count = np.int32(0)
# synchronous generators
generator_count = np.int32(0)
# utilities
utility_count = np.int32(0)

# conversion between V, A, kVar and kV, kA, MVar
voltage_units_int = np.int32(1)
current_units_int = np.int32(1)
power_units_int = np.int32(1)


opendss_iter = np.int32(300)

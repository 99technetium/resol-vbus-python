import os

# configure kind of connection "lan", "serial" or "stdin"
connection = "lan"
#connection = "serial"
#connection = "stdin"

# only used for "lan" - ip or domain name
address = ("thermal.lan", 7053)
vbus_pass = "vbus"

# only used for "serial"
port = "/dev/ttyAMA0"
baudrate = 9600

# directory containing specs files
spec_dir = os.path.dirname(__file__) + '/spec/'
# specify one or more Resol specs files to use (Python tuple / comma separated)
spec_files = ['DeltaSolBS2009.json', 'DeltaSolBX.json']
# spec_files = ['DeltaSolSLL.json']
# Deprecated - specify Resol specs file (still working but disables loading of multiple specs)
# spec_file = os.path.dirname(__file__) + '/spec/DeltaSolBS2009.json'

# expected amount of different source packets (see spec_file)
expected_packets = 2

# number of times the same packet can be received until reading is aborted
# this prevents infinite looping caused by strange behaviour of the sending controllers
# where from time to time different number of packets are sent. Also helps for too high expected_packets counts.
# Only useful for expected_packets > 1.
# Threshold of 1 means a packet can be received twice until reading is aborted, 2 means threefold ...
# Comment out or set to numbers smaller 1 to deactivate the threshold
repetitive_packets = 1

# should json data field contain units?
use_units = True

debug = False

import uhd
import numpy as np
import matplotlib
from matplotlib import pyplot
import cmath
import scipy
from scipy import signal
from time import sleep


# Create graph
graph = uhd.rfnoc.RfnocGraph("addr=10.10.23.2")

# Create FIR#0 Filter block controller and set the coefficients
fir0 = uhd.rfnoc.FirFilterBlockControl(graph.get_block("0/FIR#0"))
coefficients = [32767, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384]
fir0.set_coefficients(coefficients)
print(fir0.get_coefficients())

# Create FIR#1 Filter block controller and set the coefficients
fir1 = uhd.rfnoc.FirFilterBlockControl(graph.get_block("0/FIR#1"))
coefficients = [24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576, 24576]
fir1.set_coefficients(coefficients)
print(fir1.get_coefficients())

# Create rx and tx streamer
sa = uhd.usrp.StreamArgs('fc32', 'sc16')
sa.args = "spp=128"
rx_streamer = graph.create_rx_streamer(1, sa)
tx_streamer = graph.create_tx_streamer(1, sa)

# Connect graph
graph.connect(tx_streamer, 0, "0/SplitStream#0", 0)
graph.connect("0/SplitStream#0", 0, "0/FIR#0", 0, False)
graph.connect("0/SplitStream#0", 1, "0/FIR#1", 0, False)
graph.connect("0/FIR#0", 0, "0/AddCom#0", 0, False)
graph.connect("0/FIR#1", 0, "0/AddCom#0", 1, False)
graph.connect("0/AddCom#0", 0, rx_streamer, 0)

# Commit blocks
for edge in graph.enumerate_active_connections():
    print(edge.to_string())

graph.commit()

# Create input
input_data = np.zeros((1, 1000), dtype=np.complex64)
input_data[0, 0] = (1.0)

# matplotlib.pyplot.plot(input_data[0].real, 'r', input_data[0].imag, 'b')
# matplotlib.pyplot.show()

# Send data
tx_md = uhd.types.TXMetadata()
tx_md.start_of_burst = True
tx_md.end_of_burst = True
num_sent = tx_streamer.send(input_data, tx_md)
print("{}\n".format(num_sent))

# Receive data
output_data = np.zeros((1, 1000), dtype=np.complex64)
rx_md = uhd.types.RXMetadata()
num_recv = rx_streamer.recv(output_data, rx_md, 1.0)
print("{}\n{}".format(num_recv, rx_md))

# Shows output data - If everything is fine this should show the impulse response which is the array of coefficients of the FIR filter
output_plot = output_data[0, 0:41]
matplotlib.pyplot.plot(output_plot.real, 'r.', output_plot.imag, 'b.')
matplotlib.pyplot.savefig('complex_fir.png')
matplotlib.pyplot.show()
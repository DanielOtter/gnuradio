#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: RFNoC: Fir Test
# GNU Radio version: v3.9.6.0-5-g797c819d

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd



from gnuradio import qtgui

class fir_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RFNoC: Fir Test", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RFNoC: Fir Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fir_test")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.rfnoc_graph = uhd_rfnoc_graph_0 = uhd.rfnoc_graph(uhd.device_addr(",".join(('addr=10.10.23.3', ''))))

        ##################################################
        # Blocks
        ##################################################
        self.uhd_rfnoc_tx_streamer_0 = uhd.rfnoc_tx_streamer(
            self.rfnoc_graph,
            1,
            uhd.stream_args(
                cpu_format="fc32",
                otw_format="sc16",
                channels=[],
                args="",
            ),
            1
        )
        self.uhd_rfnoc_rx_streamer_0 = uhd.rfnoc_rx_streamer(
            self.rfnoc_graph,
            1,
            uhd.stream_args(
                cpu_format="fc32",
                otw_format="sc16",
                channels=[],
                args="",
            ),
            1,
            True
        )
        self.blocks_probe_rate_0 = blocks.probe_rate(gr.sizeof_gr_complex*1, 500.0, 0.15)
        self.blocks_message_debug_0 = blocks.message_debug(True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_probe_rate_0, 'rate'), (self.blocks_message_debug_0, 'print'))
        self.rfnoc_graph.connect(self.uhd_rfnoc_tx_streamer_0.get_unique_id(), 0, self.uhd_rfnoc_rx_streamer_0.get_unique_id(), 0, True if "duc" in "uhd_rfnoc_rx_streamer_0" and self.uhd_rfnoc_rx_streamer_0.get_propagation() else False)
        self.connect((self.analog_noise_source_x_0, 0), (self.uhd_rfnoc_tx_streamer_0, 0))
        self.connect((self.uhd_rfnoc_rx_streamer_0, 0), (self.blocks_probe_rate_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fir_test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_uhd_rfnoc_graph_0(self):
        return self.uhd_rfnoc_graph_0

    def set_uhd_rfnoc_graph_0(self, uhd_rfnoc_graph_0):
        self.uhd_rfnoc_graph_0 = uhd_rfnoc_graph_0




def main(top_block_cls=fir_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

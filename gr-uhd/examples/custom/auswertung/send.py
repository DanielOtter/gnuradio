#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: RFNoC: Send
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

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import uhd



from gnuradio import qtgui

class send(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RFNoC: Send", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RFNoC: Send")
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

        self.settings = Qt.QSettings("GNU Radio", "send")

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
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0 = 2.45e9
        self.rfnoc_graph = uhd_rfnoc_graph_0 = uhd.rfnoc_graph(uhd.device_addr(",".join(('addr=10.10.23.2', ''))))

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_entry_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_entry_0_tool_bar.addWidget(Qt.QLabel("'variable_qtgui_entry_0'" + ": "))
        self._variable_qtgui_entry_0_line_edit = Qt.QLineEdit(str(self.variable_qtgui_entry_0))
        self._variable_qtgui_entry_0_tool_bar.addWidget(self._variable_qtgui_entry_0_line_edit)
        self._variable_qtgui_entry_0_line_edit.returnPressed.connect(
            lambda: self.set_variable_qtgui_entry_0(eng_notation.str_to_num(str(self._variable_qtgui_entry_0_line_edit.text()))))
        self.top_layout.addWidget(self._variable_qtgui_entry_0_tool_bar)
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
        self.uhd_rfnoc_tx_radio_0 = uhd.rfnoc_tx_radio(
            self.rfnoc_graph,
            uhd.device_addr("spp:0=128"),
            -1,
            0)
        self.uhd_rfnoc_tx_radio_0.set_rate(200e6)
        self.uhd_rfnoc_tx_radio_0.set_antenna('TX/RX', 0)
        self.uhd_rfnoc_tx_radio_0.set_frequency(variable_qtgui_entry_0, 0)
        self.uhd_rfnoc_tx_radio_0.set_gain(30, 0)
        self.uhd_rfnoc_tx_radio_0.set_bandwidth(200e6, 0)
        self.uhd_rfnoc_duc_0 = uhd.rfnoc_duc(
            self.rfnoc_graph,
            uhd.device_addr(''),
            -1,
            0)
        self.uhd_rfnoc_duc_0.set_freq(0, 0, uhd.time_spec(0.0))
        self.uhd_rfnoc_duc_0.set_input_rate(20e6, 0)
        self.uhd_rfnoc_duc_0.set_propagation(False)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.rfnoc_graph.connect(self.uhd_rfnoc_duc_0.get_unique_id(), 0, self.uhd_rfnoc_tx_radio_0.get_unique_id(), 0, True if "duc" in "uhd_rfnoc_tx_radio_0" and self.uhd_rfnoc_tx_radio_0.get_propagation() else False)
        self.rfnoc_graph.connect(self.uhd_rfnoc_tx_streamer_0.get_unique_id(), 0, self.uhd_rfnoc_duc_0.get_unique_id(), 0, True if "duc" in "uhd_rfnoc_duc_0" and self.uhd_rfnoc_duc_0.get_propagation() else False)
        self.connect((self.analog_const_source_x_0, 0), (self.uhd_rfnoc_tx_streamer_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "send")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_entry_0(self):
        return self.variable_qtgui_entry_0

    def set_variable_qtgui_entry_0(self, variable_qtgui_entry_0):
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_entry_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_entry_0)))
        self.uhd_rfnoc_tx_radio_0.set_frequency(self.variable_qtgui_entry_0, 0)

    def get_uhd_rfnoc_graph_0(self):
        return self.uhd_rfnoc_graph_0

    def set_uhd_rfnoc_graph_0(self, uhd_rfnoc_graph_0):
        self.uhd_rfnoc_graph_0 = uhd_rfnoc_graph_0




def main(top_block_cls=send, options=None):

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

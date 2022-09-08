#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: RFNoC: Receive
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
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd



from gnuradio import qtgui

class receive(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RFNoC: Receive", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RFNoC: Receive")
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

        self.settings = Qt.QSettings("GNU Radio", "receive")

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
        self.uhd_rfnoc_rx_radio_0 = uhd.rfnoc_rx_radio(
            self.rfnoc_graph,
            uhd.device_addr('spp=128'),
            -1,
            0)
        self.uhd_rfnoc_rx_radio_0.set_rate(200e6)
        self.uhd_rfnoc_rx_radio_0.set_antenna('RX2', 0)
        self.uhd_rfnoc_rx_radio_0.set_frequency(2.45e9, 0)
        self.uhd_rfnoc_rx_radio_0.set_gain(30, 0)
        self.uhd_rfnoc_rx_radio_0.set_bandwidth(200e6, 0)
        self.uhd_rfnoc_rx_radio_0.set_dc_offset(False, 0)
        self.uhd_rfnoc_rx_radio_0.set_iq_balance(False, 0)
        self.uhd_rfnoc_ddc_0 = uhd.rfnoc_ddc(
            self.rfnoc_graph,
            uhd.device_addr(''),
            -1,
            0)
        self.uhd_rfnoc_ddc_0.set_freq(0, 0, uhd.time_spec(0.0))
        self.uhd_rfnoc_ddc_0.set_output_rate(200e6, 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            200e6, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)


        ##################################################
        # Connections
        ##################################################
        self.rfnoc_graph.connect(self.uhd_rfnoc_ddc_0.get_unique_id(), 0, self.uhd_rfnoc_rx_streamer_0.get_unique_id(), 0, True if "duc" in "uhd_rfnoc_rx_streamer_0" and self.uhd_rfnoc_rx_streamer_0.get_propagation() else False)
        self.rfnoc_graph.connect(self.uhd_rfnoc_rx_radio_0.get_unique_id(), 0, self.uhd_rfnoc_ddc_0.get_unique_id(), 0, True if "duc" in "uhd_rfnoc_ddc_0" and self.uhd_rfnoc_ddc_0.get_propagation() else False)
        self.connect((self.uhd_rfnoc_rx_streamer_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "receive")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_uhd_rfnoc_graph_0(self):
        return self.uhd_rfnoc_graph_0

    def set_uhd_rfnoc_graph_0(self, uhd_rfnoc_graph_0):
        self.uhd_rfnoc_graph_0 = uhd_rfnoc_graph_0




def main(top_block_cls=receive, options=None):

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

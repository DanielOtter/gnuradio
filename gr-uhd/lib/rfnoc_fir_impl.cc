/* -*- c++ -*- */
/*
 * Copyright 2019 Ettus Research, a National Instruments Brand.
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "rfnoc_fir_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace uhd {

rfnoc_fir::sptr rfnoc_fir::make(rfnoc_graph::sptr graph,
                                const ::uhd::device_addr_t& block_args,
                                const int device_select,
                                const int instance)
{
    return gnuradio::get_initial_sptr(new rfnoc_fir_impl(
        rfnoc_block::make_block_ref(graph, block_args, "FIR", device_select, instance)));
}


rfnoc_fir_impl::rfnoc_fir_impl(::uhd::rfnoc::noc_block_base::sptr block_ref)
    : rfnoc_block(block_ref), fir_ref(get_block_ref<::uhd::rfnoc::fir_filter_block_control>())
{
}

rfnoc_fir_impl::~rfnoc_fir_impl() {}

/******************************************************************************
 * rfnoc_fir API
 *****************************************************************************/
void rfnoc_fir_impl::set_coefficients(const std::vector<int16_t> &coeffs)
{
    return fir_ref->set_coefficients(coeffs);
}

} /* namespace uhd */
} /* namespace gr */

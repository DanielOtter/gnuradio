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

#include "rfnoc_splitstream_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace uhd {

rfnoc_splitstream::sptr rfnoc_splitstream::make(rfnoc_graph::sptr graph,
                                const ::uhd::device_addr_t& block_args,
                                const int device_select,
                                const int instance)
{
    return gnuradio::get_initial_sptr(new rfnoc_splitstream_impl(
        rfnoc_block::make_block_ref(graph, block_args, "SplitStream", device_select, instance)));
}


rfnoc_splitstream_impl::rfnoc_splitstream_impl(::uhd::rfnoc::noc_block_base::sptr block_ref)
    : rfnoc_block(block_ref), splitstream_ref(get_block_ref<::uhd::rfnoc::split_stream_block_control>())
{
}

rfnoc_splitstream_impl::~rfnoc_splitstream_impl() {}

} /* namespace uhd */
} /* namespace gr */

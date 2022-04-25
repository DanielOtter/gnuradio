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

#include "rfnoc_addcomplexmult_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace uhd {

rfnoc_addcomplexmult::sptr rfnoc_addcomplexmult::make(rfnoc_graph::sptr graph,
                                const ::uhd::device_addr_t& block_args,
                                const int device_select,
                                const int instance)
{
    return gnuradio::get_initial_sptr(new rfnoc_addcomplexmult_impl(
        rfnoc_block::make_block_ref(graph, block_args, "AddCom", device_select, instance)));
}


rfnoc_addcomplexmult_impl::rfnoc_addcomplexmult_impl(::uhd::rfnoc::noc_block_base::sptr block_ref)
    : rfnoc_block(block_ref), addcomplexmult_ref(get_block_ref<::uhd::rfnoc::addcomplexmult_block_control>())
{
}

rfnoc_addcomplexmult_impl::~rfnoc_addcomplexmult_impl() {}

} /* namespace uhd */
} /* namespace gr */

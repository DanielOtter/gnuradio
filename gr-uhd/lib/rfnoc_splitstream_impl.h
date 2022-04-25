/* -*- c++ -*- */
/*
 * Copyright 2019 Ettus Research, a National Instruments Brand.
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_GR_UHD_RFNOC_SPLITSTREAM_IMPL_H
#define INCLUDED_GR_UHD_RFNOC_SPLITSTREAM_IMPL_H

#include <gnuradio/uhd/rfnoc_splitstream.h>
#include <uhd/rfnoc/split_stream_block_control.hpp>

namespace gr {
namespace uhd {

class rfnoc_splitstream_impl : public rfnoc_splitstream
{
public:
    rfnoc_splitstream_impl(::uhd::rfnoc::noc_block_base::sptr block_ref);
    ~rfnoc_splitstream_impl();

private:
    ::uhd::rfnoc::split_stream_block_control::sptr splitstream_ref;
};

} // namespace uhd
} // namespace gr

#endif /* INCLUDED_GR_UHD_RFNOC_SPLITSTREAM_IMPL_H */

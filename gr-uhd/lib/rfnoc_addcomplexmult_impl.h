/* -*- c++ -*- */
/*
 * Copyright 2019 Ettus Research, a National Instruments Brand.
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_IMPL_H
#define INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_IMPL_H

#include <gnuradio/uhd/rfnoc_addcomplexmult.h>
#include <uhd/rfnoc/addcomplexmult_block_control.hpp>

namespace gr {
namespace uhd {

class rfnoc_addcomplexmult_impl : public rfnoc_addcomplexmult
{
public:
    rfnoc_addcomplexmult_impl(::uhd::rfnoc::noc_block_base::sptr block_ref);
    ~rfnoc_addcomplexmult_impl();

private:
    ::uhd::rfnoc::addcomplexmult_block_control::sptr addcomplexmult_ref;
};

} // namespace uhd
} // namespace gr

#endif /* INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_IMPL_H */

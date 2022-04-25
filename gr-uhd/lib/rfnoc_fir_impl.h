/* -*- c++ -*- */
/*
 * Copyright 2019 Ettus Research, a National Instruments Brand.
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_GR_UHD_RFNOC_FIR_IMPL_H
#define INCLUDED_GR_UHD_RFNOC_FIR_IMPL_H

#include <gnuradio/uhd/rfnoc_fir.h>
#include <uhd/rfnoc/fir_filter_block_control.hpp>

namespace gr {
namespace uhd {

class rfnoc_fir_impl : public rfnoc_fir
{
public:
    rfnoc_fir_impl(::uhd::rfnoc::noc_block_base::sptr block_ref);
    ~rfnoc_fir_impl();

    /*** API *****************************************************************/
    void set_coefficients(const std::vector<int16_t> &coeffs);


private:
    ::uhd::rfnoc::fir_filter_block_control::sptr fir_ref;
};

} // namespace uhd
} // namespace gr

#endif /* INCLUDED_GR_UHD_RFNOC_FIR_IMPL_H */

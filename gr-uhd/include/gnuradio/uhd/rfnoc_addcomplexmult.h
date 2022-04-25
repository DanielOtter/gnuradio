/* -*- c++ -*- */
/*
 * Copyright 2019 Ettus Research, a National Instruments Brand.
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_H
#define INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_H

#include <gnuradio/uhd/api.h>
#include <gnuradio/uhd/rfnoc_block.h>

namespace gr {
namespace uhd {

/*! RFNoC AddComplexMult
 *
 * \ingroup uhd_blk
 */
class GR_UHD_API rfnoc_addcomplexmult : virtual public rfnoc_block
{
public:
    typedef std::shared_ptr<rfnoc_addcomplexmult> sptr;

    /*!
     * \param graph Reference to the rfnoc_graph object this block is attached to
     * \param block_args Additional block arguments
     * \param device_select Device Selection
     * \param instance Instance Selection
     */
    static sptr make(rfnoc_graph::sptr graph,
                     const ::uhd::device_addr_t& block_args,
                     const int device_select,
                     const int instance);
};

} // namespace uhd
} // namespace gr

#endif /* INCLUDED_GR_UHD_RFNOC_ADDCOMPLEXMULT_H */
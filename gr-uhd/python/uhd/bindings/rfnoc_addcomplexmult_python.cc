/*
 * Copyright 2021 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(rfnoc_addcomplexmult.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(ac3cf8feaf207d93442bba4972669714)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/uhd/rfnoc_addcomplexmult.h>
// pydoc.h is automatically generated in the build directory
#include <rfnoc_addcomplexmult_pydoc.h>

void bind_rfnoc_addcomplexmult(py::module& m)
{

    using rfnoc_addcomplexmult = ::gr::uhd::rfnoc_addcomplexmult;


    py::class_<rfnoc_addcomplexmult,
               gr::uhd::rfnoc_block,
               gr::block,
               gr::basic_block,
               std::shared_ptr<rfnoc_addcomplexmult>>(m, "rfnoc_addcomplexmult", D(rfnoc_addcomplexmult))

        .def(py::init(&rfnoc_addcomplexmult::make),
             py::arg("graph"),
             py::arg("block_args"),
             py::arg("device_select"),
             py::arg("instance"),
             D(rfnoc_addcomplexmult, make))

        ;
}

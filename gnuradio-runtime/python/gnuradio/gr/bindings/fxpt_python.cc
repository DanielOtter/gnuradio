/*
 * Copyright 2020 Free Software Foundation, Inc.
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
/* BINDTOOL_HEADER_FILE(fxpt.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(f6f6a6028a7944b8a1032337bba08124)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/fxpt.h>
// pydoc.h is automatically generated in the build directory
#include <fxpt_pydoc.h>

void bind_fxpt(py::module& m)
{

    using fxpt = ::gr::fxpt;


    py::class_<fxpt, std::shared_ptr<fxpt>>(m, "fxpt", D(fxpt))

        .def(py::init<>(), D(fxpt, fxpt, 0))
        .def(py::init<gr::fxpt const&>(), py::arg("arg0"), D(fxpt, fxpt, 1))


        .def_static("float_to_fixed",
                    &fxpt::float_to_fixed,
                    py::arg("x"),
                    D(fxpt, float_to_fixed))


        .def_static("fixed_to_float",
                    &fxpt::fixed_to_float,
                    py::arg("x"),
                    D(fxpt, fixed_to_float))


        .def_static("sin", &fxpt::sin, py::arg("x"), D(fxpt, sin))


        .def_static("cos", &fxpt::cos, py::arg("x"), D(fxpt, cos))


        .def_static("sincos",
                    &fxpt::sincos,
                    py::arg("x"),
                    py::arg("s"),
                    py::arg("c"),
                    D(fxpt, sincos))

        ;
}
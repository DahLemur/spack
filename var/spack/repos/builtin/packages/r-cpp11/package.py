# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpp11(RPackage):
    """A C++11 Interface for R's C Interface.

    Provides a header only, C++11 interface to R's C interface. Compared to
    other approaches 'cpp11' strives to be safe against long jumps from the C
    API as well as C++ exceptions, conform to normal R function semantics and
    supports interaction with 'ALTREP' vectors."""

    cran = "cpp11"

    version('0.4.2', sha256='403ce0bf82358d237176053b0fb1e958cb6bfa4d0fb3555bf5801db6a6939b99')
    version('0.4.0', sha256='1768fd07dc30dfbbf8f3fb1a1183947cb7e1dfd909165c4d612a63c163a41e87')
    version('0.2.5', sha256='6fef9306c0c3043252c987e77c99ef679b2ea46dffafae318dbeb38ad21a2e20')

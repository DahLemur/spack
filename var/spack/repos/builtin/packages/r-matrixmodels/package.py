# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixmodels(RPackage):
    """Modelling with Sparse and Dense Matrices.

    Modelling with sparse and dense 'Matrix' matrices, using modular prediction
    and response module classes."""

    cran = "MatrixModels"

    version('0.5-0', sha256='a87faf1a185219f79ea2307e6787d293e1d30bf3af9398e8cfe1e079978946ed')
    version('0.4-1', sha256='fe878e401e697992a480cd146421c3a10fa331f6b37a51bac83b5c1119dcce33')

    depends_on('r@3.0.1:', type=('build', 'run'))
    depends_on('r-matrix@1.1-5:', type=('build', 'run'))

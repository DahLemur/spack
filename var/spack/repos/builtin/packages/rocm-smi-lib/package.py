# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
import shutil

from spack.package import *


class RocmSmiLib(CMakePackage):
    """It is a C library for Linux that provides a user space interface
       for applications to monitor and control GPU applications."""

    homepage = "https://github.com/RadeonOpenCompute/rocm_smi_lib"
    git      = "https://github.com/RadeonOpenCompute/rocm_smi_lib.git"
    url      = "https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-5.1.3.tar.gz"

    maintainers = ['srekolam', 'arjun-raj-kuppala']

    version('master', branch='master')
    version('5.1.3', sha256='8a19ce60dc9221545aa50e83e88d8c4be9bf7cde2425cefb13710131dc1d7b1b')
    version('5.1.0', sha256='21b31b43015b77a9119cf4c1d4ff3864f9ef1f34e2a52a38f985a3f710dc5f87')
    version('5.0.2', sha256='a169129e4ecd1cca134039dc1bf91e1b3721768781abfae4ae61fad60a633472')
    version('5.0.0', sha256='9d0e560072f815b441528a5d6124e901570a5a04e9cff1f21329861609b37203')
    version('4.5.2', sha256='d4a34db26852defb62817aa44f08ef96d678c63a6f33425bc9d48c18e5e37b7a')
    version('4.5.0', sha256='43a2cc2ec548cc28698ca4fa01a947a4414febd433936a8d9770bf6f6ed55e4f')
    version('4.3.1', sha256='ea2f9d8a9999e4aac1cb969e6bf2a9f0b6d02f29d0c319b36cce26412ab8a8b0', deprecated=True)
    version('4.3.0', sha256='c3ff56a14d334cb688a2e9a748dac46d9c2f7f576fe1f53416b1a0edbe842f8b', deprecated=True)
    version('4.2.0', sha256='c31bf91c492f00d0c5ab21e45afbd7baa990e4a8d7ce9b01e3b988e5fdd53f50', deprecated=True)
    version('4.1.0', sha256='0c1d2152e40e14bb385071ae16e7573290fb9f74afa5ab887c54f4dd75849a6b', deprecated=True)
    version('4.0.0', sha256='93d19229b5a511021bf836ddc2a9922e744bf8ee52ee0e2829645064301320f4', deprecated=True)
    version('3.10.0', sha256='8bb2142640d1c6bf141f19accf809e61377a6e0c0222e47ac4daa5da2c85ddac', deprecated=True)
    version('3.9.0', sha256='b2934b112542af56de2dc1d5bffff59957e21050db6e3e5abd4c99e46d4a0ffe', deprecated=True)
    version('3.8.0', sha256='86250c9ae9dfb18d4f7259a5f2f09b21574d4996fe5034a739ce63a27acd0082', deprecated=True)
    version('3.7.0', sha256='72d2a3deda0b55a2d92833cd648f50c7cb64f8341b254a0badac0152b26f1391', deprecated=True)
    version('3.5.0', sha256='a5d2ec3570d018b60524f0e589c4917f03d26578443f94bde27a170c7bb21e6e', deprecated=True)

    variant('build_type', default='Release', values=("Release", "Debug", "RelWithDebInfo"), description='CMake build type')
    variant('shared', default=True, description='Build shared or static library')

    depends_on('cmake@3:', type='build')
    depends_on('python@3:', type=('build', 'run'), when='@3.9.0:')

    patch('disable_pdf_generation_with_doxygen_and_latex.patch', when='@4.5.2:')

    def cmake_args(self):
        return [
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared')
        ]

    @run_after('install')
    def post_install(self):
        shutil.rmtree(self.prefix.lib)
        install_tree(self.prefix.rocm_smi,  self.prefix)
        shutil.rmtree(self.prefix.rocm_smi)
        os.remove(join_path(self.prefix.bin, 'rsmiBindings.py'))
        symlink('../bindings/rsmiBindings.py',
                join_path(self.prefix.bin, 'rsmiBindings.py'))

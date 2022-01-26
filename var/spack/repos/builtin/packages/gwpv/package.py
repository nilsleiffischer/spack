# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gwpv(PythonPackage):
    """Visualize gravitational waves with ParaView"""

    homepage = "https://github.com/nilsleiffischer/gwpv"
    url      = "https://github.com/nilsleiffischer/gwpv/archive/refs/tags/v0.2.0.tar.gz"
    git      = "https://github.com/nilsleiffischer/gwpv.git"

    maintainers = ['nilsleiffischer']

    version('master', branch='master')
    version('0.2.0', sha256='26f4adedccab15a5e188d4a097b44513b51d59380bf1d5144fc79f8e53be39ef')

    variant('gui', default=False, description="Integrate with the ParaView GUI")

    depends_on('python@3.7:')
    depends_on('paraview+python3+hdf5', when='~gui')
    depends_on('paraview+python3+hdf5+qt', when='+gui')
    
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-h5py')
    depends_on('py-spherical')
    depends_on('py-pyyaml')
    depends_on('py-tqdm')
    depends_on('py-astropy')
    depends_on('py-matplotlib')
    depends_on('py-requests')

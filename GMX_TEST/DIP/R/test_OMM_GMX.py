#!/usr/bin/env python
from __future__ import division, print_function
from collections import defaultdict

import sys

# OpenMM Imports
import simtk.openmm as mm
import simtk.openmm.app as app
import parmed as pmd
# ParmEd Imports
from parmed import load_file, unit as u
from parmed.charmm import CharmmParameterSet
from parmed.openmm import StateDataReporter, energy_decomposition_system
#params = CharmmParameterSet('parmed_par_oplsaam.inp')
top = load_file('topol.top', xyz='GMX_R.pdb')

#ala5_gas =  load_file('GP.psf')
#ala5_crds = load_file('plt.pdb')

# Create the OpenMM system
print('Creating OpenMM System')
system = top.createSystem(nonbondedMethod=app.NoCutoff,nonbondedCutoff=1000.0*u.angstroms)
# Create the integrator to do Langevin dynamics
integrator = mm.LangevinIntegrator(
                        300*u.kelvin,       # Temperature of heat bath
                        1.0/u.picoseconds,  # Friction coefficient
                        2.0*u.femtoseconds, # Time step
)

# Define the platform to use; CUDA, OpenCL, CPU, or Reference. Or do not specify
# the platform to use the default (fastest) platform
platform = mm.Platform.getPlatformByName('Reference')
sim = app.Simulation(top.topology, system, integrator, platform)
sim.context.setPositions(top.positions)

# Minimize the energy
print('Minimizing energy')
struct=pmd.load_file('GMX_R.pdb')
ecomps=(pmd.openmm.energy_decomposition_system(struct,system))
tot_ene=0.0
for i in range(0,len(ecomps)):
        tot_ene+=ecomps[i][1]
        print(ecomps[i][0],ecomps[i][1])
print('Total-energy %6.6f'%tot_ene)

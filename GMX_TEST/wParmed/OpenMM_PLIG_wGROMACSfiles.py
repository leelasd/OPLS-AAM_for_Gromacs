#!/usr/bin/env python
from sys import stdout,exit
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import parmed as pmd
from parmed import load_file
top = load_file('topol.top', xyz='complex_box_wSPCE_ions.gro')
print('Creating OpenMM System')
system = top.createSystem(nonbondedMethod=PME,nonbondedCutoff=10.0*angstroms)
platform = Platform.getPlatformByName('CUDA')
integrator = LangevinIntegrator(300*kelvin, 1/picosecond,  0.001*picoseconds)
system.addForce(MonteCarloBarostat(1*atmospheres, 300*kelvin, 25))
simulation = Simulation(top.topology, system, integrator,platform)
simulation.context.setPositions(top.positions)
## MINIMIZING 
simulation.minimizeEnergy(tolerance=0.1*kilojoule/mole, maxIterations=500)
position = simulation.context.getState(getPositions=True).getPositions()
PDBFile.writeFile(simulation.topology, position, open('boxmin.pdb', 'w'))
simulation.reporters.append(StateDataReporter(stdout, 1000, step=True,potentialEnergy=True, temperature=True,progress=True,totalSteps=100000))
simulation.step(100000)
## Setting up simulation for 10ps
TOT_STEPS = 50000000
simulation.reporters.append(StateDataReporter('data_out.csv', 10, step=True,potentialEnergy=True, temperature=True,progress=True,totalSteps=TOT_STEPS))
simulation.step(TOT_STEPS)

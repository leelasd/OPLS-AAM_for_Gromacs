import os
from collections import OrderedDict
import sys

fil = open('energy.xvg').readlines()
GMX_dat = [float(f)/4.184 for f in fil[-1].split()[1:-1]]
nfil = open('LOG_NAMD').readlines()
for line in nfil: 
    if 'ENERGY:     200' in line:  
        NAMD_DAT = [float(f) for f in line.split()[2:12]] 
print(NAMD_DAT)
print('BOND_DIFF: %5.5f'%(GMX_dat[0]-NAMD_DAT[0]))
print('ANGL_DIFF: %5.5f'%(GMX_dat[1]-NAMD_DAT[1]))
print('TORS_DIFF: %5.5f'%(GMX_dat[2]-NAMD_DAT[2]))
print('IMPR_DIFF: %5.5f'%(GMX_dat[3]-NAMD_DAT[3]))
print('ELEC_DIFF: %5.5f'%(GMX_dat[5]+GMX_dat[7]-NAMD_DAT[4]))
print('VDWL_DIFF: %5.5f'%(GMX_dat[4]+GMX_dat[6]-NAMD_DAT[5]))
print('TOTL_DIFF: %5.5f'%(GMX_dat[8]-NAMD_DAT[9]))

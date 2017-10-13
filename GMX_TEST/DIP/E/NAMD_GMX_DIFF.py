import os
from collections import OrderedDict
import sys

fil = open('energy.xvg').readlines()
GMX_dat = [float(f)/4.184 for f in fil[-1].split()[1:-1]]
nfil = open('LOG_NAMD').readlines()
for line in nfil: 
    if 'ENERGY:       0' in line:  
        NAMD_DAT = [float(f) for f in line.split()[2:12]] 
        break
#print(NAMD_DAT)
#print(GMX_dat)
print('GMX: %6.3f NAMD: %6.3f BOND_DIFF: %5.5f'%(GMX_dat[0],NAMD_DAT[0],GMX_dat[0]-NAMD_DAT[0]))
print('GMX: %6.3f NAMD: %6.3f ANGL_DIFF: %5.5f'%(GMX_dat[1],NAMD_DAT[1],GMX_dat[1]-NAMD_DAT[1]))
print('GMX: %6.3f NAMD: %6.3f TORS_DIFF: %5.5f'%(GMX_dat[2],NAMD_DAT[2],GMX_dat[2]-NAMD_DAT[2]))
print('GMX: %6.3f NAMD: %6.3f IMPR_DIFF: %5.5f'%(GMX_dat[3],NAMD_DAT[3],GMX_dat[3]-NAMD_DAT[3]))
print('GMX: %6.3f NAMD: %6.3f ELEC_DIFF: %5.5f'%(GMX_dat[5]+GMX_dat[7],NAMD_DAT[4],(GMX_dat[5]+GMX_dat[7])-(NAMD_DAT[4])))
print('GMX: %6.3f NAMD: %6.3f VDWL_DIFF: %5.5f'%(GMX_dat[4]+GMX_dat[6],NAMD_DAT[5],GMX_dat[4]+GMX_dat[6]-NAMD_DAT[5]))
print('GMX: %6.3f NAMD: %6.3f TOTL_DIFF: %5.5f'%(GMX_dat[8],NAMD_DAT[9],GMX_dat[8]-NAMD_DAT[9]))

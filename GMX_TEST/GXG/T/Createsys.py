import os
import numpy as np
import sys 

def get_Boundaries(file_name):
    pdblines=open('%s'%file_name,'r').readlines()
    coos={'X':[],'Y':[],'Z':[]}
    for line in pdblines:
        if 'ATOM' in line[0:4]:
           cs=line[27:55].split()
           coos['X'].append(float(cs[0]))
           coos['Y'].append(float(cs[1]))
           coos['Z'].append(float(cs[2]))
    DIMS={}
    DIMS['mX']= (np.max(coos['X']) - np.min(coos['X'])) +2.0
    DIMS['mY']= (np.max(coos['Y']) - np.min(coos['Y'])) +2.0
    DIMS['mZ']= (np.max(coos['Z']) - np.min(coos['Z'])) +2.0
    DIMS['CENT']=[np.mean(coos['X']),np.mean(coos['Y']),np.mean(coos['Z'])]
    print(DIMS)
    return DIMS

def setup_psf(pdb):
    pgn=open('setup.pgn','w+')
    pgn.write('''
package require psfgen   
topology top_opls_aam.inp

mol new %s  
package require autopsf  
autopsf -protein -mol 0 -prefix GP -top top_opls_aam.inp 
exit
'''%(pdb))
    pgn.close()
    test=os.system('/Applications/VMD\ 1.9.2.app/Contents/vmd/vmd_MACOSXX86 -dispdev text -e setup.pgn')
    return test



### CREATE THE SYSTEMS FOR MD SIMULATIONS 
pdb_file = sys.argv[1]
#dims = get_Boundaries(pdb_file)
setup_psf(pdb_file)


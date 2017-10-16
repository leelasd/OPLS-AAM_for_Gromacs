## PDB_FILE SHOULD THE COMPLETE PATH OF THE FILE
## REPLACE BNZ with LIGAND resname 
## USAGE: Chimera --nogui --script "prep_prot_lig.py 4w52.pdb BNZ" 
import chimera
from DockPrep import prep
import Midas
import sys
import os
PDB_file = sys.argv[1] 
lig_name = sys.argv[2]
os.system('grep ATOM %s > %s_clean.pdb'%(PDB_file,PDB_file[:-4]))
os.system('grep %s  %s > %s.pdb'%(lig_name,PDB_file,lig_name))
protein=chimera.openModels.open('%s_clean.pdb'%PDB_file[:-4])
ligand=chimera.openModels.open('%s.pdb'%lig_name)
prep(protein,addHFunc=None,addCharges=False)
prep(ligand)
Midas.write(protein,None,"protein_clean.pdb")
Midas.write(ligand,None,"ligand_wH.pdb")

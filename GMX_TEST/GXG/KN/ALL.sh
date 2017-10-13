i=$1
python Createsys.py DIP_${i}.pdb 
namd2 min.conf > LOG_NAMD
cp plt_min.coor plt.pdb 
gmx pdb2gmx -f plt.pdb -o GMX_${i}.pdb -water none

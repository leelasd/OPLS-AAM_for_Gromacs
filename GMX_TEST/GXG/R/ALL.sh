i=$1
python Createsys.py DIP_${i}.pdb 
namd2 min.conf > LOG_NAMD
cp plt_min.coor plt.pdb 
namd2 SPM.conf > LOG_NAMD

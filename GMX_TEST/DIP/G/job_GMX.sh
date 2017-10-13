i=$1
#echo '16' | gmx pdb2gmx -f plt.pdb -o GMX_${i}.pdb -water none
gmx grompp -f em.mdp -c GMX_${i}.pdb -o em.tpr 
gmx mdrun -deffnm em
echo '1 2 3 4 5 6 7 8 9 11 0' | gmx energy -f em.edr
python NAMD_GMX_DIFF.py >DIFF_LOG 
cat DIFF_LOG

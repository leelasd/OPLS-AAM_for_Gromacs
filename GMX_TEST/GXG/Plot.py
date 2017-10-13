import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('LIST',header=None)
df.columns = ['RES']
def resname2dat(resname):
    ndf = pd.read_csv(resname+'/DIFF_LOG',header=None,delim_whitespace=True)
    ndf.columns = ['GMX','GMX_ENE','NAMD','NAMD_ENE','DIFF','DIFF_ENE']
    return(ndf.set_index(['DIFF'])['DIFF_ENE'].to_dict())
comp_dict = {resname:resname2dat(resname) for resname in df.RES}
res = pd.DataFrame(comp_dict)
res = res.T
res.columns = [i[:-1] for i in res.columns]
res = res[['ANGL_DIFF','BOND_DIFF','IMPR_DIFF','TORS_DIFF','VDWL_DIFF','ELEC_DIFF','TOTL_DIFF']]
print(res.describe())
res.plot(kind='box',rot=41)
plt.ylabel('GMX - NAMD')
plt.tight_layout()
plt.savefig('RES_ZZZ.png')

# Figure F11: closure discrepancy E of the closed single-source problem versus free coefficients, and the shell error
# eps(R) at c_l = 0.74 for the start field, the three nested levels and the continued and refined levels (continued level 2,
# level 2a, level 2b, level 3c). Reads only the saved referee result files.
import json, csv, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B='referee/'
OUT='figures/'
gauss={0.68:[('gaussian_c068_n10',101),('gaussian_c068_n20',401)],0.74:[('gaussian_c074_n10',101),('gaussian_c074_n20',401)]}
nested={0.68:[('c068_level1',405)],0.74:[('c074_level1',405),('c074_level2',783),('c074_level3',1601)]}
rows=[]
fig,ax=plt.subplots(1,2,figsize=(12,4.6))
for c,col in ((0.68,'tab:blue'),(0.74,'tab:red')):
    for fam,lst,mk,ls in (('Gaussian bumps, not nested',gauss[c],'s','--'),('nested C4 splines, free tails',nested[c],'o','-')):
        sub='t1nk' if fam.startswith('Gauss') else 't1nk2'
        n=[];E=[]
        for name,nf in lst:
            d=json.load(open(B+sub+'/results/'+name+'/summary.json')); n.append(nf); E.append(d['E'])
            rows.append(dict(c_l=c,family=fam,field=name,free_coefficients=nf,E=d['E'],K=d['K']))
        ax[0].plot(n,E,marker=mk,ls=ls,color=col,label='c_l = %.2f, %s'%(c,fam))
# continued level 2 (783), angular refinement level 2a (1175), radial refinement level 2b (1391), angular refinement level 3c
# (1855), c_l = 0.74
n=[];E=[]
for sub,name,nf in (('t1nk3','c074_level2',783),('t1nk3','c074_level2a',1175),('t1nk4','c074_level2b',1391),('t1nk5','c074_level3c',1855)):
    d=json.load(open(B+sub+'/results/'+name+'/summary.json')); assert d['free_coefficients']==nf; n.append(nf); E.append(d['E'])
    rows.append(dict(c_l=0.74,family='nested C4 splines, continued and refined',field=name+' ('+sub+')',free_coefficients=nf,E=d['E'],K=d['K']))
ax[0].plot(n,E,marker='^',ls='-.',color='tab:purple',label='c_l = 0.74, nested, continued and refined')
ax[0].axhline(1e-2,color='k',lw=0.8,ls=':'); ax[0].text(110,1.1e-2,'criterion E = 1e-2',fontsize=8)
ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].set_xlabel('free coefficients'); ax[0].set_ylabel('E (RMS relative shell error, 0.02 <= R <= 50)')
ax[0].set_title('(a) closed single-source problem: E per trial space'); ax[0].legend(fontsize=7,loc='upper right')
srows=[]
for name,sub,lab in (('gaussian_c074_n20','t1nk','start: Gaussian, 401'),('c074_level1','t1nk2','nested level 1, 405'),
                     ('c074_level2','t1nk2','nested level 2, 783'),('c074_level3','t1nk2','nested level 3, 1601'),
                     ('c074_level2a','t1nk3','level 2a (angular refinement), 1175'),('c074_level2b','t1nk4','level 2b (radial refinement), 1391'),
                     ('c074_level3c','t1nk5','level 3c (angular refinement), 1855')):
    g=np.load(B+sub+'/results/'+name+'/grid.npz')
    R=np.exp(g['shell_x']); eps=g['shell_eps']
    if 'far_shell_x' in g.files:
        R=np.concatenate([R,np.exp(g['far_shell_x'])]); eps=np.concatenate([eps,g['far_shell_eps']])
    ax[1].plot(R,eps,label=lab)
    for r,e in zip(R,eps): srows.append(dict(field=name+' ('+sub+')',R=float(r),eps=float(e)))
ax[1].set_xscale('log'); ax[1].set_yscale('log'); ax[1].set_xlabel('R'); ax[1].set_ylabel('relative shell error eps(R)')
ax[1].set_title('(b) c_l = 0.74: shell error versus radius'); ax[1].legend(fontsize=7)
fig.suptitle('Approximate fields, not solutions: no level reaches the criterion',fontsize=9)
fig.tight_layout(); fig.savefig(OUT+'F11_closed_single_source.png',dpi=130)
with open(OUT+'F11a_E_per_space.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
with open(OUT+'F11b_shell_error.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(srows[0])); w.writeheader(); w.writerows(srows)
print(json.dumps(rows,indent=0))

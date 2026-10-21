from pathlib import Path
import sys,json,copy
import numpy as np
import torch
from linearized import direction_coefficients,LinearDensity
from collocation import NodalDensity
source=NodalDensity('numerics/data/dnSB_n120m48.npz')
f=torch.load('numerics/runs/ritz_n120m48_S.pt',weights_only=True,map_location='cpu')
V=f['Wv'].numpy()[:,::-1][:,:6].copy()
meta=json.loads(Path('numerics/runs/ritz_n120m48_S.json').read_text())
assert np.max(np.abs(V[-2]-np.array([r['dcl'] for r in meta['ritz_vectors'][:6]])))<1e-14
q,theta=np.meshgrid(source.qnodes[1:],source.thetanodes,indexing='ij')
cal=np.r_[(q*q*(1-q)*np.cos(4*theta)).ravel(),0.,0.];cal/=np.linalg.norm(cal)
V=np.column_stack((V,cal));labels=np.array([f'ritz{i}' for i in range(6)]+['own_smooth_calibration'])
np.savez_compressed('verifier/inverse/verification/dnSB_directions.npz',V=V,labels=labels)
co=direction_coefficients(source,V);rows=[]
for i in range(V.shape[1]):
 df=LinearDensity(source,co[:,:,i],V[-2,i]);fplus=copy.copy(source);fminus=copy.copy(source)
 for pt in [(1.,.5),(8.6,.1),(1.,1000.),(100.,1000.)]:
  exact=float(df(*pt));fd=[]
  for h in [.01,.001,.0001]:
   fplus.cl=source.cl+h*V[-2,i];fplus.k=1/fplus.cl;fplus.co=source.co+h*co[:,:,i]
   fminus.cl=source.cl-h*V[-2,i];fminus.k=1/fminus.cl;fminus.co=source.co-h*co[:,:,i]
   val=float((fplus(*pt)-fminus(*pt))/(2*h));fd.append({'h':h,'value':val,'error':val-exact})
  rows.append({'direction':labels[i],'point':pt,'algebraic_derivative':exact,'finite_differences':fd})
Path('verifier/inverse/verification/parameter_derivative_check.json').write_text(json.dumps(rows,indent=2)+'\n')
print('prepared',V.shape,'max smallest-h error',max(abs(x['finite_differences'][-1]['error']) for x in rows))

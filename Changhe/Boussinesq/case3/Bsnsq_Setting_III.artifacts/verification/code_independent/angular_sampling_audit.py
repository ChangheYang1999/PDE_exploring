"""Independent NumPy/SciPy audit of a mathematically proved angular nullspace."""
import os
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
from pathlib import Path
import hashlib,json,datetime
import numpy as np
from scipy.interpolate import BSpline
root=Path('verification/angular_sampling_20261020T2044')
snapshot=Path('verification/characteristic_a021hr_20261020T2029/state_snapshot.npz')
with np.load(snapshot,allow_pickle=False) as d:
 meta={k:d[k].item() for k in ['K','Nt','deg','grade','Nphi','L','beta_basis']}
K,Nt,p=int(meta['K']),int(meta['Nt']),int(meta['deg'])
N=12; phi=np.pi*(np.arange(N)+.5)/N
C=np.cos(phi[:,None]*np.arange(K))
edges=np.linspace(0,1,Nt+1)**meta['grade']; knots=np.r_[np.zeros(p),edges,np.ones(p)]
nb=len(knots)-p-1
j=max(9,p+2)
assert knots[j]>0 and knots[j+p+1]<1 and j>=7
b=np.zeros(nb);b[j]=1
spl=BSpline(knots,b,p)
t=np.linspace(knots[j],knots[j+p+1],53)
rad=spl(t)
rows=[]
for name,ks in [('mode12',[12]),('modes13plus11',[13,11]),('modes14plus10',[14,10]),('modes15plus9',[15,9])]:
 v=np.zeros(K);v[ks]=1
 deriv=-np.sin(phi[:,None]*np.arange(K))*np.arange(K)
 densephi=np.linspace(0,np.pi,10001)
 field=rad[:,None]*(C@v)[None,:]
 rows.append(dict(name=name,indices=ks,max_nodal_abs=float(abs(field).max()),max_dense_angular_value=float(abs(np.cos(densephi[:,None]*np.arange(K))@v).max()),max_nodal_angular_derivative=float(abs(deriv@v).max())))
ns={}
for n in [12,16,24,32]:
 cp=np.cos((np.pi*(np.arange(n)+.5)/n)[:,None]*np.arange(K))
 ns[str(n)]={'rank':int(np.linalg.matrix_rank(cp,tol=1e-12)),'singular_values':np.linalg.svd(cp,compute_uv=False).tolist()}
provenance={}
for path in ['../numerics/code/bq3core.py','../numerics/code/charnewton.py','../numerics/code/picard_a0.py','../numerics/runs/a0c1hr.log','../numerics/runs/a0c1hros.log']:
 src=Path(path);dest=root/'code_snapshot'/src.name;dest.write_bytes(src.read_bytes())
 provenance[path]={'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'snapshot':str(dest)}
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'state_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'metadata':meta,'radial_basis_count':nb,'nullity_lower_bound':4*nb-26,'test_radial_index':j,'tests':rows,'angular_ranks':ns,'source_snapshots':provenance,'scope':'Exact rank deficiency of the value fits, not a claimed nullspace of the nonlinear PDE or solver map.'}
(root/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['metadata','radial_basis_count','nullity_lower_bound','tests','angular_ranks']},indent=2))
